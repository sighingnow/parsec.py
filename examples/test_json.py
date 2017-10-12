#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test the implementation of JSON text parser in json.py.
'''

__author__ = 'He Tao, sighingnow@gmail.com'

import unittest

from parsec import *
from jsonc import *


class TestJsonc(unittest.TestCase):
    '''Test the implementation of JSON parser.'''

    def test_simple(self):
        self.assertEqual(
            jsonc.parse('{"a": "true", "b": false, "C": ["a", "b", "C"]}'),
            {"a": "true", "b": False, "C": ["a", "b", "C"]})

    def test_number(self):
        self.assertEqual(jsonc.parse('{"a": 10.00}'), {"a": 10.00})
        self.assertRaises(ParseError, jsonc.parse, '{"a": e10.00}')

    def test_quoted(self):
        self.assertEqual(jsonc.parse('{"a": "b"}'), {"a": "b"})
        self.assertEqual(jsonc.parse('{"a": "b\\""}'), {"a": "b\""})

    def test_array(self):
        result = jsonc.parse('{"a": ["a", ["b", true], "d"]}')
        self.assertEqual(result["a"], ["a", ["b", True], "d"])
        self.assertRaises(ParseError, jsonc.parse,
                          '{"a": ["a", ["b", true], "d"}')

        self.assertRaises(ParseError, jsonc.parse,
                          '{"a": ["a", "b", true], "d"}')

    def test_nest(self):
        result = jsonc.parse('''
            {
                "a": {
                    "a": "x",
                    "b": "t",
                    "c": {
                        "a": true,
                        "c": [true, false, true]
                    }
                }
            }
        ''')
        self.assertEqual(result['a']['a'], 'x')
        self.assertEqual(result['a']['c']['a'], True)
        self.assertEqual(result['a']['c']['c'], [True, False, True])

    def test_empty(self):
        self.assertEqual(jsonc.parse('{}'), {})
        result = jsonc.parse('{"a":[]}')
        self.assertEqual(result['a'], [])

if __name__ == '__main__':
    unittest.main()
