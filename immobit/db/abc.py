"""
Database models definitions
"""
from homeinfo.his.api.db import HISServiceDatabase
from homeinfolib import HIModel

__date__ = '09.10.2014'
__author__ = 'Richard Neumann <r.neumannr@homeinfo.de>'


class ImmobitModel(HIModel):
    """
    A generic model / table inside the ImmoBit database
    """
    class Meta:
        database = HISServiceDatabase('immobit')
        schema = database.database
