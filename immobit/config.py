"""ImmoBit's main configuration."""

from configlib import INIParser

__all__ = ['CONFIG']


CONFIG = INIParser('/etc/immobit.conf')
