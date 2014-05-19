# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ember_demo
version = ember_demo.__version__

setup(
    name='ember_demo',
    version=version,
    author='',
    author_email='andrew@agconti.com',
    packages=[
        'ember_demo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['ember_demo/manage.py'],
)