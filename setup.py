#! /usr/bin/env python3

from setuptools import setup


setup(
    name="immobit",
    use_scm_version={"local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm"],
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info@homeinfo.de>",
    maintainer="Richard Neumann",
    maintainer_email="<r.neumann@homeinfo.de>",
    install_requires=[
        "flask",
        "his",
        "mdb",
        "openimmodb",
        "peewee",
        "peeweeplus",
        "wsgilib",
    ],
    packages=["immobit", "immobit.wsgi"],
    description="Immobit",
)
