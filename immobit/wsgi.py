"""WSGI interface."""

from traceback import format_exc

from peewee import DoesNotExist

from openimmodb import OpenImmoDBError, IncompleteDataError, InvalidDataError,\
    ConsistencyError, Transaction, Immobilie, Kontakt, Anhang, \
    RealEstateExists as RealEstateExists_, \
    AttachmentExists as AttachmentExists_
from wsgilib import JSON, Error, InternalServerError, OK, Binary

from his.api.messages import NotAnInteger, InvalidUTF8Data, InvalidJSON
from his.api.handlers import AuthorizedService

from his.mods.fs.orm import Inode

from .messages import InvalidRealEstateID, NoRealEstateSpecified, \
    NoSuchRealEstate, RealEstatedCreated, CannotAddRealEstate, \
    RealEstateExists, RealEstateDeleted, CannotDeleteRealEstate, \
    NoRealEstateDataProvided, NoAttachmentSpecified, AttachmentCreated, \
    AttachmentExists, AttachmentDeleted, NoSuchAttachment, \
    NoDataForAttachment, AttachmentLimitExceeded, ForeignAttachmentAccess
from .orm import TransactionLog, CustomerPortal

__all__ = [
    'RealEstates',
    'Attachments',
    'Contacts',
    'HANDLERS']


def pages(limit, real_estates):
    """Returns the amout of possible
    pages for the specified limit.
    """

    if limit is None:
        return 1

    if real_estates % limit:
        return real_estates // limit + 1

    return real_estates // limit


def mkpage(page, limit, real_estates):
    """Yields real estates from page no. <page> of size <size>."""

    first = page * limit
    last = (page + 1) * limit

    for index, real_estate in enumerate(real_estates):
        if first <= index < last:
            yield real_estate


class AbstractCommonHanlderBase(AuthorizedService):
    """Real estate aware service."""

    ERRORS = {
        'NO_DATA_PROVIDED': NoRealEstateDataProvided(),
        'NON_UTF8_DATA': InvalidUTF8Data(),
        'NON_JSON_DATA': InvalidJSON()}

    @property
    def real_estates(self):
        """Yields real estates of the current customer."""
        return Immobilie.select().where(Immobilie.customer == self.customer)

    @property
    def real_estate(self):
        """Returns the specified real estate."""
        try:
            record_id = int(self.resource)
        except TypeError:
            raise NoRealEstateSpecified() from None
        except ValueError:
            raise InvalidRealEstateID() from None
        else:
            try:
                return Immobilie.get(
                    (Immobilie.customer == self.customer) &
                    (Immobilie.id == record_id))
            except DoesNotExist:
                raise NoSuchRealEstate() from None


class RealEstates(AbstractCommonHanlderBase):
    """Handles requests for ImmoBit."""

    NODE = 'realestates'

    @property
    def limit(self):
        """Returns the set limit of real estates per page."""
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
        """Returns the selected page number."""
        try:
            page = self.query['page']
        except KeyError:
            return 0
        else:
            try:
                return int(page)
            except (ValueError, TypeError):
                raise NotAnInteger('page', page) from None

    def transaction_log(self, action, objektnr_extern):
        """Returns a new transaction log entry."""
        return TransactionLog(
            account=self.account, customer=self.customer,
            objektnr_extern=objektnr_extern, action=action)

    def _list(self):
        """Lists available reale states."""
        return JSON([re.short_dict() for re in self.real_estates])

    def _page(self):
        """Returns the appropriate page."""
        real_estates = list(self.real_estates)
        page = self.page
        limit = self.limit
        return JSON({
            'immobilie': [
                real_estate.short_dict() for real_estate in
                mkpage(page, limit, real_estates)],
            'page': page,
            'limit': limit,
            'pages': pages(limit, len(real_estates))}, strip=False)

    def _add(self, dictionary):
        """Adds the real estate represented by the dictionary."""
        try:
            with Transaction(logger=self.logger) as transaction:
                ident = transaction.add(self.customer, dictionary=dictionary)
        except RealEstateExists_:
            raise RealEstateExists() from None
        except IncompleteDataError as error:
            raise Error('Incomplete data: {}'.format(
                error.element), status=422) from None
        except ConsistencyError:
            raise Error('Data inconsistent', status=422) from None
        except OpenImmoDBError:
            raise InternalServerError('Unspecified database error:\n{}'.format(
                format_exc())) from None
        else:
            return (transaction, ident)

    def _patch(self, immobilie, dictionary):
        """Adds the real estate represented by the dictionary."""
        try:
            with Transaction(logger=self.logger) as transaction:
                transaction.patch(immobilie, dictionary=dictionary)
        except IncompleteDataError as error:
            raise Error('Incomplete data: {}'.format(
                error.element), status=422) from None
        except InvalidDataError as error:
            raise Error(str(error), status=422) from None
        except RealEstateExists_:
            raise RealEstateExists() from None
        except ConsistencyError:
            raise Error('Data inconsistent', status=422) from None
        except OpenImmoDBError:
            raise Error('Unspecified database error:\n{}'.format(
                format_exc())) from None
        else:
            return transaction

    def get(self):
        """Returns available real estates."""
        if self.resource is None:
            if self.query.get('count', False):
                return JSON({'count': len(list(self.real_estates))})

            if self.limit is None:
                return self._list()

            return self._page()

        return JSON(self.real_estate.to_dict(), strip=False, status=200)

    def post(self):
        """Adds new real estates."""
        dictionary = self.data.json

        try:
            objektnr_extern = dictionary['verwaltung_techn']['objektnr_extern']
        except (KeyError, TypeError):
            objektnr_extern = None

        with self.transaction_log('CREATE', objektnr_extern) as log:
            transaction, ident = self._add(dictionary)

            if transaction:
                log.success = True
                return RealEstatedCreated(id=ident)

            raise CannotAddRealEstate() from None

    def delete(self):
        """Removes real estates."""
        immobilie = self.real_estate

        with self.transaction_log('DELETE', immobilie.objektnr_extern) as log:
            try:
                immobilie.remove()
            except OpenImmoDBError:
                self.logger.error(
                    'Could not delete real estate:\n{}'.format(
                        format_exc()))
                raise CannotDeleteRealEstate() from None
            else:
                log.success = True
                return RealEstateDeleted()

    def patch(self):
        """Partially updates real estates."""
        immobilie = self.real_estate

        with self.transaction_log('UPDATE', immobilie.objektnr_extern) as log:
            if self._patch(immobilie, self.data.json):
                log.success = True
                return OK('Real estate patched')
            else:
                raise InternalServerError(
                    'Could not patch real estate:\n{}'.format(
                        format_exc())) from None

    def options(self):
        """Returns options information."""
        return OK()


class Attachments(AbstractCommonHanlderBase):
    """Handles requests for ImmoBit."""

    NODE = 'realestates'
    REAL_ESTATE_LIMIT = 15
    CUSTOMER_LIMIT = 2000

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def anhang(self):
        """Returns the respective Anhang ORM model."""
        try:
            aid = int(self.resource)
        except TypeError:
            raise NoAttachmentSpecified() from None
        except ValueError:
            raise NoSuchAttachment() from None
        else:
            try:
                anhang = Anhang.get(Anhang.id == aid)
            except DoesNotExist:
                raise NoSuchAttachment() from None
            else:
                if anhang.immobilie.customer == self.customer:
                    return anhang
                else:
                    raise ForeignAttachmentAccess() from None

    @property
    def _data(self):
        """Returns the attachment data."""
        if not self.data.bytes:
            raise NoDataForAttachment() from None
        else:
            try:
                sha256sum = self.data.bytes.decode()
            except ValueError:
                return self.data.bytes
            else:
                for inode in Inode.by_sha256(sha256sum):
                    if inode.readable_by(self.account):
                        return inode.data

                raise NoDataForAttachment() from None

    def get(self):
        """Gets the respective data."""
        if self.resource is None:
            raise NoAttachmentSpecified() from None
        else:
            return Binary(self.anhang.data)

    def post(self):
        """Adds an attachment."""
        if self.resource is None:
            raise NoRealEstateSpecified()

        immobilie = self.real_estate

        if Anhang.count(immobilie=immobilie) < self.REAL_ESTATE_LIMIT:
            if Anhang.count(customer=self.customer) < self.CUSTOMER_LIMIT:
                try:
                    anhang = Anhang.from_bytes(self._data, immobilie)
                except AttachmentExists_:
                    raise AttachmentExists() from None
                else:
                    anhang.save()
                    return AttachmentCreated(id=anhang.id)

        raise AttachmentLimitExceeded() from None

    def put(self):
        """Uploads metadata into an existing attachment."""
        return self.patch()

    def patch(self):
        """Modifies metadata of an existing attachment."""
        self.anhang.patch(self.data.json).save()
        return OK()

    def delete(self):
        """Deletes an attachment."""
        self.anhang.remove()
        return AttachmentDeleted()

    def options(self):
        """Returns options information."""
        return OK()


class Contacts(AbstractCommonHanlderBase):
    """Service to retrieve contacts."""

    NODE = 'realestates'

    @property
    def contacts(self):
        """Yields appropriate contacts."""
        for immobilie in self.real_estates:
            for kontakt in Kontakt.select().where(
                    Kontakt.immobilie == immobilie):
                yield kontakt

    def get(self):
        """Returns appropriate contacts."""
        if self.resource is not None:
            raise Error('Contacts can only be listed.') from None
        else:
            return JSON([c.to_dict() for c in self.contacts])


class Portals(AuthorizedService):
    """Yields customer portals."""

    NODE = 'realestates'

    @property
    def customer_portals(self):
        """Yields appropriate customer <> portal mappings."""
        return CustomerPortal.select().where(
            CustomerPortal.customer == self.customer)

    @property
    def portals(self):
        """Yields appropriate portals."""
        for customer_portal in self.customer_portals:
            yield customer_portal.portal

    def get(self):
        """Returns the respective portals."""
        return JSON(list(self.portals), strip=False)


HANDLERS = {
    'realestates': RealEstates,
    'attachments': Attachments,
    'contacts': Contacts,
    'portals': Portals}
