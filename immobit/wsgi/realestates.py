"""Real estates API."""

from traceback import format_exc

from flask import request

from his import ACCOUNT, CUSTOMER, authenticated, authorized
from openimmodb import ConsistencyError
from openimmodb import Immobilie
from openimmodb import IncompleteDataError
from openimmodb import InvalidDataError
from openimmodb import OpenImmoDBError
from openimmodb import RealEstateExists
from openimmodb import Transaction
from wsgilib import JSON, Browser, Error

from immobit.messages import CANNOT_ADD_REAL_ESTATE
from immobit.messages import CANNOT_DELETE_REAL_ESTATE
from immobit.messages import NO_SUCH_REAL_ESTATE
from immobit.messages import REAL_ESTATE_CREATED
from immobit.messages import REAL_ESTATE_DELETED
from immobit.messages import REAL_ESTATE_EXISTS
from immobit.messages import REAL_ESTATE_UPDATED
from immobit.orm import TransactionLog


__all__ = ['ROUTES', 'get_real_estate', 'get_real_estates']


BROWSER = Browser()


def _transaction(action, objektnr_extern):
    """Returns a new transaction log entry."""

    return TransactionLog(
        account=ACCOUNT.id, customer=CUSTOMER.id,
        objektnr_extern=objektnr_extern, action=action)


def _add_real_estate(dictionary):
    """Adds the real estate represented by the dictionary."""

    try:
        with Transaction() as transaction:
            ident = transaction.add(CUSTOMER.id, dictionary=dictionary)
    except RealEstateExists:
        raise REAL_ESTATE_EXISTS
    except IncompleteDataError as incomplete_data_error:
        raise JSON(incomplete_data_error.to_dict(), status=422)
    except ConsistencyError as consistency_error:
        raise Error(str(consistency_error), status=422)
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
        raise JSON(incomplete_data_error.to_dict(), status=422)
    except InvalidDataError as invalid_data_error:
        raise JSON(invalid_data_error.to_dict(), status=422)
    except RealEstateExists:
        raise REAL_ESTATE_EXISTS
    except ConsistencyError as consistency_error:
        raise Error(str(consistency_error), status=422)
    except OpenImmoDBError:
        raise JSON({
            'message': 'Unspecified database error.',
            'stacktrace': format_exc()}, status=500)

    return transaction


def get_real_estate(ident):
    """Returns the specified real estate."""

    try:
        return Immobilie.get(
            (Immobilie.customer == CUSTOMER.id) & (Immobilie.id == ident))
    except Immobilie.DoesNotExist:
        raise NO_SUCH_REAL_ESTATE


def get_real_estates():
    """Yields real estates of the current customer."""

    return Immobilie.select().where(Immobilie.customer == CUSTOMER.id)


@authenticated
@authorized('immobit')
def lst():
    """Returns available real estates."""

    real_estates = get_real_estates()

    if BROWSER.wanted:
        if BROWSER.info:
            return BROWSER.pages(real_estates).to_json()

        real_estates = BROWSER.browse(real_estates)

    return JSON([real_estate.short_dict() for real_estate in real_estates])


@authenticated
@authorized('immobit')
def get(ident):
    """Returns the respective real estate."""

    return JSON(get_real_estate(ident).to_dict())


@authenticated
@authorized('immobit')
def add():
    """Adds a new real estate."""

    try:
        objektnr_extern = request.json['verwaltung_techn']['objektnr_extern']
    except (KeyError, TypeError):
        objektnr_extern = None

    with _transaction('CREATE', objektnr_extern) as log:
        transaction, ident = _add_real_estate(request.json)

        if transaction:
            log.success = True

    if log.success:
        return REAL_ESTATE_CREATED.update(id=ident)

    raise CANNOT_ADD_REAL_ESTATE


@authenticated
@authorized('immobit')
def delete(ident):
    """Removes a real estate."""

    real_estate = get_real_estate(ident)

    with _transaction('DELETE', real_estate.objektnr_extern) as log:
        try:
            real_estate.delete_instance()
        except OpenImmoDBError:
            raise CANNOT_DELETE_REAL_ESTATE.update(stacktrace=format_exc())

        log.success = True

    if log.success:
        return REAL_ESTATE_DELETED

    raise CANNOT_DELETE_REAL_ESTATE


@authenticated
@authorized('immobit')
def patch(ident):
    """Partially updates real estates."""

    real_estate = get_real_estate(ident)

    with _transaction('UPDATE', real_estate.objektnr_extern) as log:
        if _patch_real_estate(real_estate, request.json):
            log.success = True

    if log.success:
        return REAL_ESTATE_UPDATED

    raise JSON({
        'message': 'Could not patch real estate.',
        'stacktrace': format_exc(),
        'patch': request.json}, status=500)


ROUTES = (
    ('GET', '/realestates', lst, 'list_real_estates'),
    ('GET', '/realestates/<int:ident>', get, 'get_real_estate'),
    ('POST', '/realestates', add, 'add_real_estate'),
    ('DELETE', '/realestates/<int:ident>', delete, 'delete_real_estate'),
    ('PATCH', '/realestates/<int:ident>', patch, 'patch_real_estate'))
