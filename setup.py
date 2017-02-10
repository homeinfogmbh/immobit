#! /usr/bin/env python3

from distutils.core import setup
from homeinfo.lib.misc import GitInfo

version, author, author_email, *_ = GitInfo()

setup(
    name='his.realestates',
    version=version,
    author=author,
    author_email=author_email,
    requires=['his'],
    package_dir={'his.mods': ''},
    packages=['his.mods.realestates'],
    data_files=[
        ('/etc/his.d/locale', ['files/etc/his.d/locale/realestates.ini']),
    description='Immobit')
