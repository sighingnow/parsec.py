#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'parsec.py',
    version = '1.0.0',
    description = 'A univeral Python parser combinator library inspirted by Parsec library of Haskell.',
    author = 'He Tao',
    author_email = 'sighingnow@gmail',
    url = 'https://github.com/sighignow/parsec.py',
    license = 'MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Compilers",
        "License :: OSI Approved :: MIT License",
    ],
    keywords = 'monad parser combinator',

    package_dir={'': 'src'},
    packages=find_packages('src'),
)


