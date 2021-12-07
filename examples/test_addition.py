'''
Test the implementation of the addition parser in addition.py.
'''

import unittest

from parsec import *
from addition import *

test_strings = (
        ('1', 1),
        ('123', 123),
        ('(( 123))', 123),
        ('((1+2))', 3),
        ('1+2+3', 6),
        ('1+2+3+4', 10),
        ('(4 + 5 + 2)', 11),
        ('(4 + 5) + 2', 11),
        ('2 + (4 + 5)', 11),
        ('2 + (5 + (3+4))', 14),
        ('2 + ((3+4) + 20)', 29),
        ('2 + (5 + (3+4) + 5)', 19),
        ('2 + (5 + (3+4) + (3+2 + (5)))', 24),
)


class TestAddition(unittest.TestCase):
    '''Test the implementation of the addition parser.'''

    def test_addition_simple(self):
        for expr_str, expected in test_strings:
            self.assertEqual(
                expr.parse(expr_str),
                expected)

if __name__ == '__main__':
    unittest.main()
