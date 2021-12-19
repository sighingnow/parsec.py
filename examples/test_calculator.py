'''
Test the implementation of the addition parser in addition.py.
'''

import unittest

from parsec import *
from calculator import *

test_strings = (
        ('1', 1),
        ('123', 123),
        ('(( 123))', 123),
        ('(( 1+2))', 3),
        ('1+2+3', 6),
        ('1+2+3+4', 10),
        ('(4 + 5 + 2)', 11),
        ('(4 + 5) + 2', 11),
        ('2 + (4 + 5)', 11),
        ('2 + (5 + (3+4))', 14),
        ('2 + ((3+4) + 20)', 29),
        ('2 + (5 + (3+4) + 5)', 19),
        ('2 + (5 + (3+4) + (3+2 + (5)))', 24),
        ('2 * 5', 10),
        ('2 * (5 + 7)', 24),
        ('((2 * 5) + 7)', 17),
        ('(((2 * 5) + 7))', 17),
        (' 2 * 5 + 7', 17),
        ('10 - 3 - 4', 3),
        (' 2 * 5 - 7', 3),
        (' 7 - 2 * 2', 3),
        ('7 + -1', 6),
        ('-7 + -1', -8),
        ('-7 + -1', -8),
        ('1 + 3 -2', 2),
        ('(1 - 3) +2', 0),
        ('1 - 3 +2', 0),
        ('1 -7 + -1', -7),
        (' ((1 -7)) + -1', -7),
        ('2 * 3 / 2', 3),
        ('2 * 3 + 4 / 2', 8),
        (' 2 - 2 * 3 + 4 / 2 ', -2),
        ('2--2', 4),
        ('-2', -2),
)

bad_test_strings = (
    '2++2',
    '2-+-2',
    '2**2',
    ' 2- ',
    '2+',
    '+2',
)


class TestAddition(unittest.TestCase):
    '''Test the implementation of the addition parser.'''

    def test_addition_simple(self):
        for expr_str, expected in test_strings:
            print(f'parsing: {expr_str}')
            self.assertEqual(
                full_expr.parse(expr_str),
                expected)

    def test_bad_strings(self):
        for bad_expr_str in bad_test_strings:
            print(f'parsing: {bad_expr_str}')
            self.assertRaises(ParseError, full_expr.parse, bad_expr_str)

if __name__ == '__main__':
    unittest.main()
