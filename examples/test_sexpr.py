#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test the implementation of $-expression parser in sexpr.py.
'''

__author__ = 'He Tao, sighingnow@gmail.com'

import unittest

from parsec import *
from sexpr import *


class TestSexpr(unittest.TestCase):
    '''Test the implementation of $-expression parser.'''

    def test_form(self):
        result = program.parse('(1 2 3)')
        self.assertEqual(result, [[1, 2, 3]])

    def test_quote(self):
        result = program.parse("'foo '(bar baz)")
        self.assertEqual(result,
                         [['quote', 'foo'], ['quote', ['bar', 'baz']]])

    def test_double_quote(self):
        result = program.parse("''foo")
        self.assertEqual(result, [['quote', ['quote', 'foo']]])

    def test_op(self):
        result = program.parse('+-*/+-*/')
        self.assertEqual(result, ['+', '-', '*', '/', '+', '-', '*', '/'])

    def test_boolean(self):
        result = program.parse('#t #f')
        self.assertEqual(result, [True, False])

    def test_comments(self):
        result = program.parse('''
            ; a program with a comment
            (           foo ; that's a foo
            bar )
            ; some comments at the end
        ''')

        self.assertEqual(result, [['foo', 'bar']])

if __name__ == '__main__':
    unittest.main()
