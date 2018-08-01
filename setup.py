#! /usr/bin/env python3

from distutils.core import setup


setup(
    name='immobit',
    version='latest',
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info at homeinfo dot de>',
    maintainer='Richard Neumann',
    maintainer_email='<r dot neumann at homeinfo period de>',
    requires=['his'],
    packages=['immobit', 'immobit.wsgi'],
    description='Immobit')
