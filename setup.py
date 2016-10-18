#! /usr/bin/env python3

from distutils.core import setup
from homeinfo.lib.misc import GitInfo

version, author, author_email, *_ = GitInfo()

setup(
    name='his.immobit',
    version=version,
    author=author,
    author_email=author_email,
    requires=['his'],
    package_dir={'his.mods': ''},
    packages=['his.mods.immobit'],
    description='Immobit')
