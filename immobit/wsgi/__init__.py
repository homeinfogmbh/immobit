"""WSGI interface."""

from wsgilib import Application

from immobit.wsgi import attachments, contacts, portals, realestates

__all__ = ['APPLICATION']


ENDPOINTS = {}
ENDPOINTS.update(attachments.ENDPOINTS)
ENDPOINTS.update(contacts.ENDPOINTS)
ENDPOINTS.update(portals.ENDPOINTS)
ENDPOINTS.update(realestates.ENDPOINTS)
APPLICATION = Application('ImmoBit', debug=True, cors=True)
APPLICATION.add_endpoints(ENDPOINTS)
