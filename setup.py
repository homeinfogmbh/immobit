#! /usr/bin/env python3

from distutils.core import setup


setup(
    name='immobit',
    version='latest',
    author='Richard Neumann',
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
