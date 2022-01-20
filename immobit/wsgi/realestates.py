"""Real estates API."""

from traceback import format_exc
from typing import Any

from flask import request
from peewee import Select

from his import ACCOUNT, CUSTOMER, authenticated, authorized
from openimmodb import ConsistencyError
from openimmodb import Immobilie
from openimmodb import IncompleteDataError
from openimmodb import InvalidDataError
from openimmodb import RealEstateExists
from openimmodb import Transaction
from wsgilib import Browser, Error, JSON, JSONMessage

from immobit.enumerations import Action
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


def _transaction(action: Action, objektnr_extern: str) -> TransactionLog:
    """Returns a new transaction log entry."""

    return TransactionLog(
        account=ACCOUNT.id, customer=CUSTOMER.id,
        objektnr_extern=objektnr_extern, action=action
    )


def _add_real_estate(json: dict[str, Any]) -> tuple[Transaction, int]:
    """Adds the real estate represented by a JSON-ish dict."""

    try:
        with Transaction() as transaction:
            ident = transaction.add(CUSTOMER.id, json=json)
    except RealEstateExists:
        raise REAL_ESTATE_EXISTS
    except IncompleteDataError as incomplete_data_error:
        raise JSON(incomplete_data_error.to_json(), status=422)
    except ConsistencyError as consistency_error:
        raise Error(str(consistency_error), status=422)

    return transaction, ident


def _patch_real_estate(
        immobilie: Immobilie, json: dict[str, Any]
) -> Transaction:
    """Adds the real estate represented by a JSON-ish dict."""

    try:
        with Transaction() as transaction:
            transaction.patch(immobilie, json)
    except IncompleteDataError as incomplete_data_error:
        raise JSON(incomplete_data_error.to_json(), status=422)
    except InvalidDataError as invalid_data_error:
        raise JSON(invalid_data_error.to_json(), status=422)
    except RealEstateExists:
        raise REAL_ESTATE_EXISTS
    except ConsistencyError as consistency_error:
        raise Error(str(consistency_error), status=422)

    return transaction


def get_real_estate(ident: int) -> Immobilie:
    """Returns the specified real estate."""

    try:
        return Immobilie.get(
            (Immobilie.customer == CUSTOMER.id) & (Immobilie.id == ident))
    except Immobilie.DoesNotExist:
        raise NO_SUCH_REAL_ESTATE


def get_real_estates() -> Select:
    """Yields real estates of the current customer."""

    return Immobilie.select().where(Immobilie.customer == CUSTOMER.id)


@authenticated
@authorized('immobit')
def lst() -> JSON:
    """Returns available real estates."""

    real_estates = get_real_estates()

    if BROWSER.wanted:
        if BROWSER.info:
            return BROWSER.pages(real_estates).to_json()

        real_estates = BROWSER.browse(real_estates)

    return JSON([real_estate.short_dict() for real_estate in real_estates])


@authenticated
@authorized('immobit')
def get(ident: int) -> JSON:
    """Returns the respective real estate."""

    return JSON(get_real_estate(ident).to_json())


@authenticated
@authorized('immobit')
def add() -> JSONMessage:
    """Adds a new real estate."""

    try:
        objektnr_extern = request.json['verwaltung_techn']['objektnr_extern']
    except (KeyError, TypeError):
        objektnr_extern = None

    with _transaction(Action.CREATE, objektnr_extern) as log:
        transaction, ident = _add_real_estate(request.json)

        if transaction:
            log.success = True

    if log.success:
        return REAL_ESTATE_CREATED.update(id=ident)

    raise CANNOT_ADD_REAL_ESTATE


@authenticated
@authorized('immobit')
def delete(ident: int) -> JSONMessage:
    """Removes a real estate."""

    real_estate = get_real_estate(ident)

    with _transaction(Action.DELETE, real_estate.objektnr_extern) as log:
        real_estate.delete_instance()
        log.success = True

    if log.success:
        return REAL_ESTATE_DELETED

    raise CANNOT_DELETE_REAL_ESTATE


@authenticated
@authorized('immobit')
def patch(ident: int) -> JSON | JSONMessage:
    """Partially updates real estates."""

    real_estate = get_real_estate(ident)

    with _transaction(Action.UPDATE, real_estate.objektnr_extern) as log:
        if _patch_real_estate(real_estate, request.json):
            log.success = True

    if log.success:
        return REAL_ESTATE_UPDATED

    raise JSON({
        'message': 'Could not patch real estate.',
        'stacktrace': format_exc(),
        'patch': request.json
    }, status=500)


ROUTES = (
    ('GET', '/realestates', lst),
    ('GET', '/realestates/<int:ident>', get),
    ('POST', '/realestates', add),
    ('DELETE', '/realestates/<int:ident>', delete),
    ('PATCH', '/realestates/<int:ident>', patch)
)
