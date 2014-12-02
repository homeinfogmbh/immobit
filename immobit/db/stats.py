"""
Statistics models
"""
from .abc import ImmobitModel
from peewee import CharField, FloatField

__date__ = '02.12.2014'
__author__ = 'Richard Neumann <r.neumannr@homeinfo.de>'
__all__ = ['Statistics']


class Statistics(ImmobitModel):
    """
    A model to represent statistics in ImmoBit
    """
    name = CharField(16)
    """The statistic's name"""
    value = FloatField()
    """The statistics value"""
    # TODO: implement
