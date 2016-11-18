#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'parsec',
    version = '3.2',
    description = 'parser combinator.',
    long_description = 'A univeral Python parser combinator library inspirted by Parsec library of Haskell.',
    author = 'He Tao',
    author_email = 'sighingnow@gmail.com',
    url = 'https://github.com/sighingnow/parsec.py',
    license = 'MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Compilers",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "License :: OSI Approved :: MIT License",
    ],
    platforms = 'any',
    keywords = 'monad parser combinator',

    package_dir = {'': 'src'},
    packages = find_packages('src'),

    test_suite = 'tests',
)

