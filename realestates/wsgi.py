"""WSGI interface"""

from json import loads
from traceback import format_exc

from peewee import DoesNotExist

from openimmodb import OpenImmoDBError, IncompleteDataError, \
    ConsistencyError, Transaction, Immobilie, Anhang
from homeinfo.lib.wsgi import JSON, Error, InternalServerError, OK, Binary

from his.api.errors import NotAnInteger
from his.api.handlers import AuthorizedService

from his.mods.fs.errors import NotReadable
from his.mods.fs.orm import Inode

from .errors import InvalidJSON, IdMismatch, \
    NoRealEstateSpecified,  NoSuchRealEstate, RealEstateExists, \
    RealEstatedCreated, RealEstateUpdated, RealEstateDeleted,  \
    NoAttachmentSpecified, AttachmentCreated, AttachmentExists, \
    AttachmentDeleted, NoSuchAttachment, NoDataForAttachment, \
    AttachmentLimitCustomerExceeded, AttachmentLimitRealEstateExceeded
from .orm import TransactionLog

__all__ = [
    'RealEstates',
    'Attachments',
    'HANDLERS']


class RealEstates(AuthorizedService):
    """Handles requests for ImmoBit"""

    NODE = 'realestates'
    NAME = 'ImmoBit'
    DESCRIPTION = 'Immobiliendatenverwaltung'
    PROMOTE = True

    @property
    def json(self):
        """Retruns JSON dict from data"""
        try:
            text = self.data.decode('utf-8')
        except UnicodeDecodeError:
            raise Error('Posted data is not UTF-8', status=415) from None
        else:
            try:
                return loads(text)
            except ValueError:
                raise Error('Invalid JSON:\n{}'.format(text),
                            status=422) from None

    @property
    def limit(self):
        """Returns the set limit of real estates per page"""
        try:
            limit = self.query['limit']
        except KeyError:
            return None
        else:
            try:
                return int(limit)
            except (ValueError, TypeError):
                raise NotAnInteger('limit', limit) from None

    @property
    def page(self):
        """Returns the selected page number"""
        try:
            page = self.query['page']
        except KeyError:
            return 0
        else:
            try:
                return int(page)
            except (ValueError, TypeError):
                raise NotAnInteger('page', page) from None

    @property
    def _real_estates(self):
        """Yields real estates of the current customer"""
        return Immobilie.select().where(Immobilie._customer == self.customer)

    def _pages(self, limit, real_estates):
        """Returns the amout of possible
        pages for the specified limit
        """
        if limit is None:
            return 1
        else:
            if real_estates % limit:
                return real_estates // limit + 1
            else:
                return real_estates // limit

    def _list(self):
        """Lists available reale states"""
        return JSON({'immobilie': [
            re.short_dict() for re in self._real_estates]})

    def _mkpage(self, page, limit, real_estates):
        """Yields real estates from page no. <page> of size <size>"""
        first = page * limit
        last = (page + 1) * limit

        for index, real_estate in enumerate(real_estates):
            if first <= index < last:
                yield real_estate

    def _page(self):
        """Returns the appropriate page"""
        real_estates = list(self._real_estates)
        page = self.page
        limit = self.limit
        return JSON({
            'immobilie': [
                real_estate.short_dict() for real_estate in
                self._mkpage(page, limit, real_estates)],
            'page': page,
            'limit': limit,
            'pages': self._pages(limit, len(real_estates))})

    def _add(self, dictionary):
        """Adds the real estate represented by the dictionary"""
        try:
            with Transaction(logger=self.logger) as transaction:
                transaction.add(self.customer, dict=dictionary)
        except IncompleteDataError as e:
            raise Error('Incomplete data: {}'.format(
                e.element), status=422) from None
        except RealEstateExists:
            raise Error('Real estate exists', status=409) from None
        except ConsistencyError:
            raise Error('Data inconsistent', status=422) from None
        except OpenImmoDBError:
            raise Error('Unspecified database error:\n{}'.format(
                format_exc())) from None
        else:
            return transaction

    def _update(self):
        """Updates a real estate"""
        dictionary = self.json

        try:
            objektnr_extern = dictionary['verwaltung_techn']['objektnr_extern']
        except KeyError:
            dictionary['verwaltung_techn']['objektnr_extern'] = self.resource
            id_match = True
        except TypeError:
            # dictionary['verwaltung_techn'] is probably None
            raise IncompleteDataError()  # XXX: todo
        else:
            id_match = objektnr_extern == self.resource

        if id_match:
            with Transaction(logger=self.logger) as t:
                try:
                    t.update(self.customer, objektnr_extern, dict=dictionary)
                except DoesNotExist:
                    raise NoSuchRealEstate() from None
                else:
                    return t
        else:
            raise IdMismatch()

    def _patch(self, dictionary):
        """Adds the real estate represented by the dictionary"""
        try:
            with Transaction(logger=self.logger) as trans:
                trans.patch(self.customer, self.resource, dict=dictionary)
        except IncompleteDataError as e:
            raise Error('Incomplete data: {}'.format(
                e.element), status=422) from None
        except RealEstateExists:
            raise Error('Real estate exists', status=409) from None
        except ConsistencyError:
            raise Error('Data inconsistent', status=422) from None
        except OpenImmoDBError:
            raise Error('Unspecified database error:\n{}'.format(
                format_exc())) from None
        else:
            return trans

    def _auth_file(self, file):
        """Determines authorization of a certain file"""
        for inode in Inode.select().where(Inode.file == file):
            if inode.readable_by(self.account):
                return True

        raise NotReadable()

    def _validate_attachment(self, attachment):
        """Validates the respective attachment"""
        try:
            file = attachment['file']
        except KeyError:
            raise IncompleteDataError('attachment.file')
        else:
            try:
                return self._auth_file(int(file))
            except (ValueError, TypeError):
                raise NotAnInteger('file', file)

    def _validate_attachments(self, attachments):
        """Validates the respective attachments"""
        for attachment in attachments:
            self._validate_attachment(attachment)

        return True

    def get(self):
        """Returns available real estates"""
        if self.resource is None:
            if self.query.get('count', False):
                return JSON({'count': len(list(self._real_estates))})
            else:
                if self.limit is None:
                    return self._list()
                else:
                    return self._page()
        else:
            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=404) from None
            else:
                return JSON(immobilie.to_dict(), status=200)

    def post(self):
        """Adds new real estates"""
        dictionary = self.json

        try:
            attachments = dictionary['anhaenge']['anhang']
        except (KeyError, TypeError):
            pass
        else:
            self._validate_attachments(attachments)

        try:
            objektnr_extern = dictionary['verwaltung_techn']['objektnr_extern']
        except (KeyError, TypeError):
            objektnr_extern = None

        with TransactionLog(
                account=self.account,
                customer=self.customer,
                objektnr_extern=objektnr_extern,
                action='CREATE') as log:
            if self._add(dictionary):
                log.success = True
                return RealEstatedCreated()
            else:
                return InternalServerError('Could not add real estate')

    def delete(self):
        """Removes real estates"""
        if self.resource is None:
            raise Error('No real estate specified', status=400) from None
        else:
            try:
                immobilie = Immobilie.fetch(self.customer, self.resource)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    self.resource), status=404) from None
            else:
                with TransactionLog(
                        account=self.account,
                        customer=self.customer,
                        objektnr_extern=self.resource,
                        action='DELETE') as log:
                    try:
                        immobilie.remove()
                    except OpenImmoDBError:
                        raise InternalServerError(
                            'Could not delete real estate:\n{}'.format(
                                format_exc())) from None
                    else:
                        log.success = True
                        return RealEstateDeleted()

    def put(self):
        """Overrides real estates"""
        if self.resource is None:
            raise NoRealEstateSpecified()
        else:
            with TransactionLog(
                    account=self.account,
                    customer=self.customer,
                    objektnr_extern=self.resource,
                    action='UPDATE') as log:
                if self._update():
                    log.success = True
                    return RealEstateUpdated()
                else:
                    return InternalServerError('Could not add real estate')

    def patch(self):
        """Partially updates real estates"""
        # XXX: DEBUG
        print('Log level:', self.logger.level, flush=True)

        if self.resource is None:
            raise Error('No real estate specified', status=400) from None
        else:
            with TransactionLog(
                    account=self.account,
                    customer=self.customer,
                    objektnr_extern=self.resource,
                    action='DELETE') as log:
                if self._patch(self.json):
                    log.success = True
                    return OK('Real estate patched')
                else:
                    raise InternalServerError(
                        'Could not patch real estate:\n{}'.format(
                            format_exc())) from None

    def options(self):
        """Returns options information"""
        return OK()


class _Attachments(AuthorizedService):
    """Handles requests for ImmoBit"""

    REAL_ESTATE_LIMIT = 15
    CUSTOMER_LIMIT = 2000

    @property
    def immobilie(self):
        """Returns the appropriate real estate"""
        objektnr_extern = self.query.get('objektnr_extern')

        if objektnr_extern is None:
            raise NoRealEstateSpecified()
        else:
            try:
                return Immobilie.fetch(self.customer, objektnr_extern)
            except DoesNotExist:
                raise Error('No such real estate: {}'.format(
                    objektnr_extern), status=404) from None

    @property
    def anhang(self):
        """Returns the respective Anhang ORM model"""
        if self.resource is None:
            raise NoAttachmentSpecified() from None
        else:
            try:
                return Anhang.get(
                    (Anhang._immobilie == self.immobilie) &
                    (Anhang.sha256sum == self.resource))
            except DoesNotExist:
                raise NoSuchAttachment() from None

    @property
    def dict(self):
        """Returns the Anhang dictionary"""
        try:
            return loads(self.data)
        except ValueError:
            raise InvalidJSON() from None
        except TypeError:
            raise NoAttachmentSpecified() from None

    @property
    def _data(self):
        """Returns the attachment data"""
        if not self.data:
            raise NoDataForAttachment() from None
        else:
            try:
                sha256sum = self.data.decode()
            except ValueError:
                return self.data
            else:
                for inode in Inode.by_sha256(sha256sum):
                    if inode.readable_by(self.account):
                        return inode.data

                raise NoDataForAttachment()

    def get(self):
        """Gets the respective data"""
        return Binary(self.anhang.to_bytes())

    def post(self):
        """Adds an attachment"""
        print('DEBUG1')
        if Anhang.count(immobilie=self.immobilie) < self.REAL_ESTATE_LIMIT:
            print('DEBUG2')
            if Anhang.count(customer=self.customer) < self.CUSTOMER_LIMIT:
                print('DEBUG3')
                try:
                    print('DEBUG4')
                    anhang = Anhang.from_bytes(self._data, self.immobilie)
                except AttachmentExists:
                    print('DEBUG5')
                    raise AttachmentExists() from None
                else:
                    print('DEBUG6')
                    anhang.save()
                    return AttachmentCreated()
            else:
                print('DEBUG7')
                raise AttachmentLimitCustomerExceeded() from None
        else:
            print('DEBUG8')
            raise AttachmentLimitRealEstateExceeded() from None

    def put(self):
        """Uploads metadata into an existing attachment"""
        return self.patch()

    def patch(self):
        """Modifies metadata of an existing attachment"""
        self.anhang.patch(self.dict).save()
        return OK()

    def delete(self):
        """Deletes an attachment"""
        self.anhang.remove()
        return AttachmentDeleted()


class Attachments(AuthorizedService):

    def post(self):
        self.logger.error('OK')


HANDLERS = {
    'data': RealEstates,
    'attachments': Attachments}
