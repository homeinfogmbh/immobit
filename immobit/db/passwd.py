"""
Abstract base classes for the ImmoBit database
"""
__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '09.10.2014'

__all__ = ['Group', 'User', 'UserGroup', 'RealEstate']

from .abc import ImmobitModel
from peewee import ForeignKeyField, TextField

class Group(ImmobitModel):
    """
    A generic, abstract ImmoBit group
    """
    name = TextField()
    """A representative name"""


class User(ImmobitModel):
    """
    A generic, abstract ImmoBit user
    """
    name = TextField()
    """A representative name"""
    passwd = TextField()
    """The user's login password"""


class UserGroup(ImmobitModel):
    """
    A generic, abstract many-to-many User <-> Group mapping
    """
    user = ForeignKeyField(User, related_name='groups')
    group = ForeignKeyField(Group, related_name='users')


class Permission(ImmobitModel):
    """
    A generic, abstract permissions table
    """
    