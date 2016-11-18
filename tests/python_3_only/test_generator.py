#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test the return with generator syntax in @generate decorate.
'''

__author__ = 'He Tao, sighingnow@gmail.com'

import unittest

from parsec import *

class ParserGeneratorWithReturnTest(unittest.TestCase):
    '''Test the implementation of Parser Generator with 'return' statement.
    '''
    def test_generate(self):
        nonlocals = {'x': None, 'y': None}
        @generate
        def fn():
            nonlocals['x'] = yield string('x')
            nonlocals['y'] = yield string('y')
            return string('z')
        self.assertEqual(fn.parse('xyz'), 'z')
        self.assertEqual(nonlocals['x'], 'x')
        self.assertEqual(nonlocals['y'], 'y')

        nonlocals = {'x': None, 'y': None}
        @generate
        def fn():
            nonlocals['x'] = yield digit()
            nonlocals['y'] = yield count(digit(), 5)
        self.assertEqual(fn.parse('123456'), None)
        self.assertEqual(nonlocals['x'], '1')
        self.assertEqual(nonlocals['y'], ['2', '3', '4', '5', '6'])

if __name__ == '__main__':
    unittest.main()
