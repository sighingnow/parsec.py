#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'parsec',
    version = '2.0.0',
    description = 'parser combinator.',
    long_description = 'A univeral Python parser combinator library inspirted by Parsec library of Haskell.',
    author = 'He Tao',
    author_email = 'sighingnow@gmail',
    url = 'https://github.com/sighignow/parsec.py',
    license = 'MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Compilers",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        "License :: OSI Approved :: MIT License",
    ],
    platforms = 'any',
    keywords = 'monad parser combinator',

    package_dir = {'': 'src'},
    packages = find_packages('src'),

    test_suite = 'tests.parsec_test',
)


