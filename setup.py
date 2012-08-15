#!/usr/bin/env python

"""The usual package management stuff."""

from setuptools import setup

import ook


setup(
    name="ook",
    author="Zero Piraeus",
    author_email="z@etiol.net",
    description=ook.__doc__,
    keywords="version sensitive monkey patch",
    license="GPLv3",
    long_description=open("README").read(),
    packages=["ook"],
    setup_requires=["setuptools_hg"],
    url="https://bitbucket.org/schesis/ook",
    version=ook.__version__,
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
