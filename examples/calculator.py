from parsec import *
from operator import add, sub, mul
from functools import partial, reduce


whitespace = regex(r'\s*', re.MULTILINE)
lexeme = lambda p: p << whitespace

lparen = lexeme(string('('))
rparen = lexeme(string(')'))

plus = lexeme(string('+'))
minus = lexeme(string('-'))
add_or_sub = plus | minus
asterisk = lexeme(string('*'))
div = lexeme(string('/'))

base_number = lexeme(regex(r'\d+').parsecmap(int))
neg_number = lexeme(string('-') >> base_number).parsecmap(lambda n: n*-1)
number = neg_number | base_number

mult_or_div = asterisk | div
peek_ops = lookahead(mult_or_div | add_or_sub | eof())

@generate
def braced():
    yield lparen
    es = yield expr
    yield rparen
    return es

@generate
def primary():
    val = yield number | braced | exclude(expr, peek_ops)
    return val

def addition_reducer(x,y):
    op, val = y
    if op == '+':
        return x + val
    elif op == '-':
        return x - val
    else:
        raise ValueError('unexpected op: {}'.format(op))

def mult_reducer(x,y):
    op, val = y
    if op == '*':
        return x * val
    elif op == '/':
        return x / val
    else:
        raise ValueError('unexpected op: {}'.format(op))

mult = (primary + sepBy(mult_or_div + primary, whitespace)).parsecmap(lambda t: reduce(mult_reducer, t[1], t[0]))
expr = (mult + sepBy(add_or_sub + mult, whitespace)).parsecmap(lambda t: reduce(addition_reducer, t[1], t[0]))

full_expr = whitespace >> expr << eof()

