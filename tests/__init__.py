#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Used as test cases loader to load all unit tests under the examples directory for parsec.py.
'''

__author__ = 'He Tao, sighingnow@gmail.com'

import unittest

def additional_tests():
    '''Accumulate all unit test cases.'''
    loader = unittest.defaultTestLoader
    additional_names = ['examples']
    suite = unittest.TestSuite()
    for name in additional_names:
        suite.addTests(loader.discover(name))
    return suite

