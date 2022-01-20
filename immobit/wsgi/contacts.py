"""Contacts API."""

from typing import Iterator

from his import authenticated, authorized
from openimmodb import Kontakt
from wsgilib import JSON

from immobit.wsgi.realestates import get_real_estates


__all__ = ['ROUTES']


def _get_contacts() -> Iterator[Kontakt]:
    """Yields appropriate contacts."""

    for immobilie in get_real_estates():
        yield from Kontakt.select().where(Kontakt.immobilie == immobilie)


@authenticated
@authorized('immobit')
def get() -> JSON:
    """Returns appropriate contacts."""

    return JSON([contact.to_json() for contact in _get_contacts()])


ROUTES = [('GET', '/contacts', get)]
