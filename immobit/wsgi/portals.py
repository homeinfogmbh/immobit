"""Real estate portals API."""

from his import CUSTOMER, authenticated, authorized
from wsgilib import JSON

from immobit.orm import CustomerPortal

__all__ = ['get_portals']


def _get_portals():
    """Yields appropriate portals."""

    for customer_portal in CustomerPortal.select().where(
            CustomerPortal.customer == CUSTOMER.id):
        yield customer_portal.portal


@authenticated
@authorized('immobit')
def get_portals():
    """Returns the respective portals."""

    return JSON(list(_get_portals()))
