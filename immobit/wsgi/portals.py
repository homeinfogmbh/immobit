"""Real estate portals API."""

from typing import Iterator

from his import CUSTOMER, authenticated, authorized
from wsgilib import JSON

from immobit.orm import CustomerPortal


__all__ = ['ROUTES']


def _get_portals() -> Iterator[str]:
    """Yields appropriate portals."""

    for customer_portal in CustomerPortal.select().where(
            CustomerPortal.customer == CUSTOMER.id
    ):
        yield customer_portal.portal


@authenticated
@authorized('immobit')
def get() -> JSON:
    """Returns the respective portals."""

    return JSON(list(_get_portals()))


ROUTES = [('GET', '/portals', get)]
