#! /usr/bin/env python3

from distutils.core import setup
from homeinfo.lib.misc import GitInfo

version, author, author_email, *_ = GitInfo()

setup(
    name='immobrowse',
    version=version,
    author=author,
    author_email=author_email,
    requires=['his'],
    packages=['immobrowse'],
    data_files=[
        ('/etc/his.d/locale',
         ['files/etc/his.d/locale/immobrowse.ini'])],
    description='Immobit')
