"""
Permissions definition tables
"""
__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '21.10.2014'

__all__ = ['ImmobitUser']

from .abc import ImmobitModel
from his.lib.db.models.passwd import User
from peewee import IntegerField, BooleanField

class ImmobitUser(ImmobitModel):
    """
    A user within the ImmoBit system
    """
    _his_user = IntegerField(db_column='his_user')
    """The identifier of the corresponding HIS user"""
    admin = BooleanField()
    """Flag, whether the user is an administrator"""
    
    @property
    def his_user(self):
        """Returns the corresponding HIS user"""
        return User.select().where(User.id == self._his_user) #@UndefinedVariable