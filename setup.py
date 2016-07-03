#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='ntv',
    version='0.4.4',
    description='n.tv api',
    long_description=readme + '\n\n' + history,
    author='Marek Wywiał',
    author_email='onjinx@gmail.com',
    url='https://github.com/onjin/ntv',
    packages=[
        'ntv',
    ],
    package_dir={'ntv': 'ntv'},
    include_package_data=True,
    install_requires=[
        'requests',
        'requests_cache',
        'simplejson',
        'clint',
        'baker',
    ],
    license="BSD",
    zip_safe=False,
    keywords='ntv',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    scripts=['ntv/ntv-cli'],
)
