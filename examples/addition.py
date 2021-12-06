from parsec import *

whitespace = regex(r'\s*', re.MULTILINE)
lexeme = lambda p: p << whitespace

lparen = lexeme(string('('))
rparen = lexeme(string(')'))

plus = lexeme(string('+'))

number = lexeme(regex(r'\d+').parsecmap(int))


@generate
def addition():
    e1 = yield (braced | number)
    yield plus
    e2 = yield expr
    return e1 + e2

@generate
def braced():
    yield lparen
    es = yield expr
    yield rparen
    return es

expr = addition ^ (braced | number)

