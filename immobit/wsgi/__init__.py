"""WSGI interface."""

from itertools import chain

from wsgilib import Application

from immobit.wsgi import attachments, contacts, portals, realestates

__all__ = ['APPLICATION']


APPLICATION = Application('ImmoBit', debug=True, cors=True)
APPLICATION.add_routes(chain(
    attachments.ROUTES, contacts.ROUTES, portals.ROUTES, realestates.ROUTES))
