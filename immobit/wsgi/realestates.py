"""Real estates API."""

from traceback import format_exc

from flask import request
from peewee import DoesNotExist

from his import ACCOUNT, CUSTOMER, DATA, authenticated, authorized
from his.messages.data import NotAnInteger
from openimmodb import OpenImmoDBError, IncompleteDataError, InvalidDataError,\
    ConsistencyError, Transaction, Immobilie, \
    RealEstateExists as RealEstateExists_
from wsgilib import JSON, OK, Error

from immobit.messages import NoSuchRealEstate, RealEstatedCreated, \
    CannotAddRealEstate, RealEstateExists, RealEstateDeleted, \
    CannotDeleteRealEstate
from immobit.orm import TransactionLog

__all__ = [
    'get_real_estates',
    'get_real_estate',
    'add_real_estate',
    'delete_real_estate',
    'patch_real_estate']


def _transaction(action, objektnr_extern):
    """Returns a new transaction log entry."""

    return TransactionLog(
        account=ACCOUNT, customer=CUSTOMER, objektnr_extern=objektnr_extern,
        action=action)


def _pages(limit, real_estates):
    """Returns the amout of possible
    pages for the specified limit.
    """

    if limit is None:
        return 1

    if real_estates % limit:
        return real_estates // limit + 1

    return real_estates // limit


def _mkpage(page, limit, real_estates):
    """Yields real estates from page no. <page> of size <size>."""

    first = page * limit
    last = (page + 1) * limit

    for index, real_estate in enumerate(real_estates):
        if first <= index < last:
            yield real_estate


def _get_real_estates():
    """Yields real estates of the current customer."""

    return Immobilie.select().where(Immobilie.customer == CUSTOMER.id)


def _get_real_estate(ident):
    """Returns the specified real estate."""

    try:
        return Immobilie.get(
            (Immobilie.customer == CUSTOMER) & (Immobilie.id == ident))
    except DoesNotExist:
        raise NoSuchRealEstate()


def _get_limit():
    """Returns the set limit of real estates per page."""

    try:
        limit = request.args['limit']
    except KeyError:
        return None

    try:
        return int(limit)
    except (ValueError, TypeError):
        raise NotAnInteger('limit', limit)


def _get_page():
    """Returns the selected page number."""

    try:
        page = request.args['page']
    except KeyError:
        return 0

    try:
        return int(page)
    except (ValueError, TypeError):
        raise NotAnInteger('page', page)


def _page_real_estates():
    """Returns the appropriate page."""
    real_estates = tuple(_get_real_estates())
    page = _get_page()
    limit = _get_limit()
    return JSON({
        'immobilie': [
            real_estate.short_dict() for real_estate in
            _mkpage(page, limit, real_estates)],
        'page': page,
        'limit': limit,
        'pages': _pages(limit, len(real_estates))}, strip=False)


def _add_real_estate(dictionary):
    """Adds the real estate represented by the dictionary."""

    try:
        with Transaction() as transaction:
            ident = transaction.add(CUSTOMER, dictionary=dictionary)
    except RealEstateExists_:
        raise RealEstateExists()
    except IncompleteDataError as incomplete_data_error:
        raise Error(str(incomplete_data_error), status=422)
    except ConsistencyError:
        raise Error('Data inconsistent', status=422)
    except OpenImmoDBError:
        raise JSON({
            'message': 'Unspecified database error.',
            'stacktrace': format_exc()}, status=500)

    return (transaction, ident)


def _patch_real_estate(immobilie, dictionary):
    """Adds the real estate represented by the dictionary."""
    try:
        with Transaction() as transaction:
            transaction.patch(immobilie, dictionary=dictionary)
    except IncompleteDataError as incomplete_data_error:
        raise Error(str(incomplete_data_error), status=422)
    except InvalidDataError as invalid_data_error:
        raise Error(str(invalid_data_error), status=422)
    except RealEstateExists_:
        raise RealEstateExists()
    except ConsistencyError:
        raise Error('Data inconsistent', status=422)
    except OpenImmoDBError:
        raise JSON({
            'message': 'Unspecified database error.',
            'stacktrace': format_exc()}, status=500)

    return transaction


@authenticated
@authorized('immobit')
def get_real_estates():
    """Returns available real estates."""

    if request.args.get('count', False):
        return JSON({'count': len(list(_get_real_estates()))})

    if _get_limit() is None:
        return JSON([re.short_dict() for re in _get_real_estates()])

    return _page_real_estates()


@authenticated
@authorized('immobit')
def get_real_estate(ident):
    """Returns the respective real estate."""

    return JSON(_get_real_estate(ident).to_dict())


@authenticated
@authorized('immobit')
def add_real_estate():
    """Adds a new real estate."""

    json = DATA.json

    try:
        objektnr_extern = json['verwaltung_techn']['objektnr_extern']
    except (KeyError, TypeError):
        objektnr_extern = None

    with _transaction('CREATE', objektnr_extern) as log:
        transaction, ident = _add_real_estate(json)

        if transaction:
            log.success = True
            return RealEstatedCreated(id=ident)

        raise CannotAddRealEstate() from None


@authenticated
@authorized('immobit')
def delete_real_estate(ident):
    """Removes a real estate."""

    real_estate = _get_real_estate(ident)

    with _transaction('DELETE', real_estate.objektnr_extern) as log:
        try:
            real_estate.remove()
        except OpenImmoDBError:
            raise CannotDeleteRealEstate(stacktrace=format_exc())

        log.success = True
        return RealEstateDeleted()


@authenticated
@authorized('immobit')
def patch_real_estate(ident):
    """Partially updates real estates."""

    real_estate = _get_real_estate(ident)

    with _transaction('UPDATE', real_estate.objektnr_extern) as log:
        if _patch_real_estate(real_estate, DATA.json):
            log.success = True
            return OK('Real estate patched.')

        raise JSON({
            'message': 'Could not patch real estate.',
            'stacktrace': format_exc()}, status=500)