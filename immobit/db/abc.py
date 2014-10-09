'''
Created on 09.10.2014

@author: neumannr
'''
from peewee import MySQLDatabase, Model

db = MySQLDatabase()

class ImmobitModel(Model):
    """
    A generic model / table inside the ImmoBit database
    """
    class Meta:
        database = db