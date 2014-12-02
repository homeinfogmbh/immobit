"""
Real estate portal configuration
"""
from .abc import ImmobitModel
from peewee import CharField

__date__ = '02.12.2014'
__author__ = 'Richard Neumann <r.neumannr@homeinfo.de>'
__all__ = ['Portal']


class FTPPortal(ImmobitModel):
    """
    A model to represent a real estate portal in immobit
    """
    name = CharField(16)
    """The portal's name"""
    user_name = CharField(16)
    """The FTP user name"""
    passwd = CharField(128)
    """The FTP user's password"""


class OAuth1Portal(ImmobitModel):
    """
    A model to represent a real estate portal in immobit
    """
    name = CharField(16)
    """The portal's name"""
    user_name = CharField(16)
    """The FTP user name"""
    access_token = CharField(36)
    """The OAuth-1.0 access token"""
    access_token_secret = CharField(108)
    """The OAuth-1.0 access token secret"""
