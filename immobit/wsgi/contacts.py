"""Contacts API."""

from his import authenticated, authorized
from openimmodb import Kontakt
from wsgilib import JSON

from immobit.wsgi.realestates import get_real_estates


__all__ = ['ROUTES']


def _get_contacts():
    """Yields appropriate contacts."""

    for immobilie in get_real_estates():
        for kontakt in Kontakt.select().where(Kontakt.immobilie == immobilie):
            yield kontakt


@authenticated
@authorized('immobit')
def get():
    """Returns appropriate contacts."""

    return JSON([contact.to_dict() for contact in _get_contacts()])


ROUTES = (('GET', '/contacts', get, 'get_contacts'),)
