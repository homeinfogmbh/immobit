#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='homeinfo-his-immobit',
    version='0.0.1-indev',
    author='Richard Neumann',
    author_email='r.neumann@homeinfo.de',
    requires=['homeinfo.his'],
    package_dir={'homeinfo.his': ''},
    packages=['homeinfo.his.immobit'],
    license=open('LICENSE.txt').read(),
    description='An online real estate exposé tool',
    long_description=open('README.txt').read())
