"""Attachments API."""

from flask import request

from his import CUSTOMER, authenticated, authorized
from openimmodb import Anhang
from wsgilib import OK, Binary

from immobit.messages import ATTACHMENT_CREATED
from immobit.messages import ATTACHMENT_DELETED
from immobit.messages import ATTACHMENT_LIMIT_EXCEEDED
from immobit.messages import NO_SUCH_ATTACHMENT
from immobit.wsgi.realestates import get_real_estate


__all__ = ['ROUTES']


REAL_ESTATE_LIMIT = 15
CUSTOMER_LIMIT = 2000


def _get_attachment(ident):
    """Returns the respective Anhang ORM model."""

    try:
        anhang = Anhang.get(Anhang.id == ident)
    except Anhang.DoesNotExist:
        raise NO_SUCH_ATTACHMENT

    if anhang.immobilie.customer.id == CUSTOMER.id:
        return anhang

    raise NO_SUCH_ATTACHMENT


@authenticated
@authorized('immobit')
def get(ident):
    """Handles requests for ImmoBit."""

    return Binary(_get_attachment(ident).bytes)


@authenticated
@authorized('immobit')
def add(ident):
    """Adds a real estate for the respective attachment."""

    real_estate = get_real_estate(ident)

    if Anhang.count(immobilie=real_estate) < REAL_ESTATE_LIMIT:
        if Anhang.count(customer=CUSTOMER.id) < CUSTOMER_LIMIT:
            anhang = Anhang.from_bytes(request.data, real_estate)
            anhang.save()
            return ATTACHMENT_CREATED.update(id=anhang.id)

    raise ATTACHMENT_LIMIT_EXCEEDED


@authenticated
@authorized('immobit')
def patch(ident):
    """Modifies metadata of an existing attachment."""

    _get_attachment(ident).patch(request.json).save()
    return OK()


@authenticated
@authorized('immobit')
def delete(ident):
    """Deletes an attachment."""

    _get_attachment(ident).delete_instance()
    return ATTACHMENT_DELETED


ROUTES = (
    ('GET', '/attachments/<int:ident>', get),
    ('POST', '/attachments/<int:ident>', add),
    (['PATCH', 'PUT'], '/attachments/<int:ident>', patch),
    ('DELETE', '/attachments/<int:ident>', delete)
)
