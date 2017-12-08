"""Contacts API."""

from his import authenticated, authorized
from openimmodb import Kontakt
from wsgilib import JSON

from immobit.wsgi.realestates import _get_real_estates

__all__ = ['get_contacts']


def _get_contacts():
    """Yields appropriate contacts."""

    for immobilie in _get_real_estates():
        for kontakt in Kontakt.select().where(Kontakt.immobilie == immobilie):
            yield kontakt


@authenticated
@authorized('immobit')
def get_contacts():
    """Returns appropriate contacts."""

    return JSON([contact.to_dict() for contact in _get_contacts()])
