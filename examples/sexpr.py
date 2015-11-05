#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Use parsec.py to parse $-expression (like expression in LISP).
'''

__author__ = 'He Tao, sighingnow@gmail.com'

from parsec import *

import re

## ignore cases.
whitespace = regex(r'\s+', re.MULTILINE)
comment    = regex(r';.*')
ignore     = many((whitespace | comment))

## lexer for words.
lexeme = lambda p: p << ignore ## skip all ignored characters.
lparen = lexeme(string('('))
rparen = lexeme(string(')'))
number = lexeme(regex(r'\d+')).parsecmap(int)
symbol = lexeme(regex(r'[\d\w_-]+'))
true   = lexeme(string('#t')).result(True)
false  = lexeme(string('#f')).result(False)
op     = lexeme(regex(r'[\+\-*/]'))

atom   = op | number | symbol | (true ^ false)

@generate('a form')
def form():
    '''Parse expression within a pair of parenthesis.'''
    yield lparen
    es = yield many(expr)
    yield rparen
    return es

@generate
def quote():
    '''Parse expression after a quote symbol.'''
    yield string("'")
    e = yield expr
    return ['quote', e]

expr    = atom | form | quote
program = ignore >> many(expr)



