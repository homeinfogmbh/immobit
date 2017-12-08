"""Attachments API."""

from peewee import DoesNotExist

from his import CUSTOMER, DATA, authenticated, authorized
from openimmodb import Immobilie, Anhang, AttachmentExists as AttachmentExists_
from wsgilib import OK, Binary

from immobit.messages import NoSuchRealEstate, AttachmentCreated, \
    AttachmentExists, AttachmentDeleted, NoSuchAttachment, \
    AttachmentLimitExceeded, ForeignAttachmentAccess

__all__ = [
    'get_attachment',
    'add_attachment',
    'patch_attachment',
    'delete_attachment']


REAL_ESTATE_LIMIT = 15
CUSTOMER_LIMIT = 2000


def _get_attachment(ident):
    """Returns the respective Anhang ORM model."""

    try:
        anhang = Anhang.get(Anhang.id == ident)
    except DoesNotExist:
        raise NoSuchAttachment()

    if anhang.immobilie.customer == CUSTOMER:
        return anhang

    raise ForeignAttachmentAccess()


def _get_real_estate(ident):
    """Returns the specified real estate."""

    try:
        return Immobilie.get(
            (Immobilie.customer == CUSTOMER)
            & (Immobilie.id == ident))
    except DoesNotExist:
        raise NoSuchRealEstate()


@authenticated
@authorized('immobit')
def get_attachment(ident):
    """Handles requests for ImmoBit."""

    return Binary(_get_attachment(ident).data)


@authenticated
@authorized('immobit')
def add_attachment(ident):
    """Adds a real estate for the respective attachment."""

    real_estate = _get_real_estate(ident)

    if Anhang.count(immobilie=real_estate) < REAL_ESTATE_LIMIT:
        if Anhang.count(customer=CUSTOMER) < CUSTOMER_LIMIT:
            try:
                anhang = Anhang.from_bytes(DATA.bytes, real_estate)
            except AttachmentExists_:
                raise AttachmentExists()

            anhang.save()
            return AttachmentCreated(id=anhang.id)

    raise AttachmentLimitExceeded()


@authenticated
@authorized('immobit')
def patch_attachment(ident):
    """Modifies metadata of an existing attachment."""

    _get_attachment(ident).patch(DATA.json).save()
    return OK()


@authenticated
@authorized('immobit')
def delete_attachment(ident):
    """Deletes an attachment."""

    _get_attachment(ident).remove()
    return AttachmentDeleted()
