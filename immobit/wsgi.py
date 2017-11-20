"""WSGI interface."""

from functools import lru_cache
from traceback import format_exc

from peewee import DoesNotExist

from openimmodb import OpenImmoDBError, IncompleteDataError, InvalidDataError,\
    ConsistencyError, Transaction, Immobilie, Kontakt, Anhang, \
    RealEstateExists as RealEstateExists_, \
    AttachmentExists as AttachmentExists_
from wsgilib import JSON, Error, InternalServerError, OK, Binary, Router

from his.api.messages import NotAnInteger, InvalidUTF8Data, InvalidJSON
from his.api.handlers import service, AuthorizedService
from his.mods.fs.orm import Inode

from immobit.messages import NoRealEstateSpecified, NoSuchRealEstate, \
    RealEstatedCreated, CannotAddRealEstate, RealEstateExists, \
    RealEstateDeleted, CannotDeleteRealEstate, NoRealEstateDataProvided, \
    NoAttachmentSpecified, AttachmentCreated, AttachmentExists, \
    AttachmentDeleted, NoSuchAttachment, NoDataForAttachment, \
    AttachmentLimitExceeded, ForeignAttachmentAccess
from immobit.orm import TransactionLog, CustomerPortal

__all__ = [
    'RealEstates',
    'Attachments',
    'Contacts',
    'ROUTER']


ROUTER = Router()


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


class RealEstatesAware(AuthorizedService):
    """Real estate aware service."""

    ERRORS = {
        'NO_DATA_PROVIDED': NoRealEstateDataProvided(),
        'NON_UTF8_DATA': InvalidUTF8Data(),
        'NON_JSON_DATA': InvalidJSON()}

    @property
    def real_estates(self):
        """Yields real estates of the current customer."""
        return Immobilie.select().where(Immobilie.customer == self.customer)


@service('immobit')
@ROUTER.route('/realestates/[id:int]')
class RealEstates(RealEstatesAware):
    """Handles requests for ImmoBit."""

    @property
    @lru_cache(maxsize=1)
    def real_estate(self):
        """Returns the specified real estate."""
        if self.vars['id'] is None:
            raise NoRealEstateSpecified() from None

        try:
            return Immobilie.get(
                (Immobilie.customer == self.customer) &
                (Immobilie.id == self.vars['id']))
        except DoesNotExist:
            raise NoSuchRealEstate() from None

    @property
    @lru_cache(maxsize=1)
    def limit(self):
        """Returns the set limit of real estates per page."""
        try:
            limit = self.query['limit']
        except KeyError:
            return None

        try:
            return int(limit)
        except (ValueError, TypeError):
            raise NotAnInteger('limit', limit) from None

    @property
    @lru_cache(maxsize=1)
    def page(self):
        """Returns the selected page number."""
        try:
            page = self.query['page']
        except KeyError:
            return 0

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
        except IncompleteDataError as incomplete_data_error:
            raise Error(str(incomplete_data_error), status=422) from None
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
        except IncompleteDataError as incomplete_data_error:
            raise Error(str(incomplete_data_error), status=422) from None
        except InvalidDataError as invalid_data_error:
            raise Error(str(invalid_data_error), status=422) from None
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
        try:
            objektnr_extern = self.data.json['verwaltung_techn'][
                'objektnr_extern']
        except (KeyError, TypeError):
            objektnr_extern = None

        with self.transaction_log('CREATE', objektnr_extern) as log:
            transaction, ident = self._add(self.data.json)

            if transaction:
                log.success = True
                return RealEstatedCreated(id=ident)

            raise CannotAddRealEstate() from None

    def delete(self):
        """Removes real estates."""
        with self.transaction_log(
                'DELETE', self.real_estate.objektnr_extern) as log:
            try:
                self.real_estate.remove()
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
        with self.transaction_log(
                'UPDATE', self.real_estate.objektnr_extern) as log:
            if self._patch(self.real_estate, self.data.json):
                log.success = True
                return OK('Real estate patched')

            raise InternalServerError(
                'Could not patch real estate:\n{}'.format(
                    format_exc())) from None

    def options(self):
        """Returns options information."""
        return OK()


@service('immobit')
@ROUTER.route('/attachments/<real_estate_id:int>/[id:int]')
class Attachments(RealEstatesAware):
    """Handles requests for ImmoBit."""

    REAL_ESTATE_LIMIT = 15
    CUSTOMER_LIMIT = 2000

    @property
    @lru_cache(maxsize=1)
    def real_estate(self):
        """Returns the specified real estate."""
        try:
            return Immobilie.get(
                (Immobilie.customer == self.customer) &
                (Immobilie.id == self.vars['real_estate_id']))
        except DoesNotExist:
            raise NoSuchRealEstate() from None

    @property
    @lru_cache(maxsize=1)
    def anhang(self):
        """Returns the respective Anhang ORM model."""
        if self.vars['id'] is None:
            raise NoAttachmentSpecified() from None

        try:
            anhang = Anhang.get(Anhang.id == self.vars['id'])
        except DoesNotExist:
            raise NoSuchAttachment() from None

        if anhang.immobilie.customer == self.customer:
            return anhang

        raise ForeignAttachmentAccess() from None

    @property
    def _data(self):
        """Returns the attachment data."""
        if not self.data.bytes:
            raise NoDataForAttachment() from None

        try:
            sha256sum = self.data.bytes.decode()
        except ValueError:
            return self.data.bytes

        for inode in Inode.by_sha256(sha256sum):
            if inode.readable_by(self.account):
                return inode.data

        raise NoDataForAttachment() from None

    def get(self):
        """Gets the respective data."""
        return Binary(self.anhang.data)

    def post(self):
        """Adds an attachment."""
        if Anhang.count(immobilie=self.real_estate) < self.REAL_ESTATE_LIMIT:
            if Anhang.count(customer=self.customer) < self.CUSTOMER_LIMIT:
                try:
                    anhang = Anhang.from_bytes(self._data, self.real_estate)
                except AttachmentExists_:
                    raise AttachmentExists() from None

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


@service('immobit')
@ROUTER.route('/contacts')
class Contacts(RealEstatesAware):
    """Service to retrieve contacts."""

    @property
    def contacts(self):
        """Yields appropriate contacts."""
        for immobilie in self.real_estates:
            for kontakt in Kontakt.select().where(
                    Kontakt.immobilie == immobilie):
                yield kontakt

    def get(self):
        """Returns appropriate contacts."""
        return JSON([c.to_dict() for c in self.contacts])


@service('immobit')
@ROUTER.route('/portals')
class Portals(AuthorizedService):
    """Yields customer portals."""

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
