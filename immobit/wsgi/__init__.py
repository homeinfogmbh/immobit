"""WSGI interface."""

from wsgilib import Application

from immobit.wsgi.attachments import *
from immobit.wsgi.realestates import *
from immobit.wsgi.contacts import *
from immobit.wsgi.portals import *

__all__ = ['APPLICATION']


APPLICATION = Application('ImmoBit')
