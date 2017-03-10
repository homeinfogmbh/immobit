#! /usr/bin/env python3

from distutils.core import setup
from homeinfo.lib.misc import GitInfo

version, author, author_email, *_ = GitInfo()

setup(
    name='immobit',
    version=version,
    author=author,
    author_email=author_email,
    requires=['his'],
    packages=['immobit'],
    data_files=[
        ('/etc/his.d/locale',
         ['files/etc/his.d/locale/immobit.ini'])],
    description='Immobit')
