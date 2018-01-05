"""Real estate portals API."""

from his import CUSTOMER, authenticated, authorized
from wsgilib import JSON

from immobit.orm import CustomerPortal

__all__ = ['ENDPOINTS']


def _get_portals():
    """Yields appropriate portals."""

    for customer_portal in CustomerPortal.select().where(
            # Must compare to ID here, since LocalProxy
            # cannot handle right handed operands.
            CustomerPortal.customer == CUSTOMER.id):
        yield customer_portal.portal


@authenticated
@authorized('immobit')
def get():
    """Returns the respective portals."""

    return JSON(list(_get_portals()))


ENDPOINTS = {'get_portals': ('GET', '/portals', get)}
