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
        ('/usr/share/his',
         ['files/usr/share/his/immobit.wsgi']),
        ('/etc/uwsgi/apps-available',
         ['files/etc/uwsgi/apps-available/immobit.ini']),
        ('/etc/his.d/locale',
         ['files/etc/his.d/locale/immobit.ini'])],
    description='Immobit')
