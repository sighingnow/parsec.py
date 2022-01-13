:Date: 2022-01-13
:Version: 3.12
:Authors: - He Tao

.. meta::
   :http-equiv=Content-Type: text/html; charset=utf-8
   :keywords: python, parser, combinator
   :description lang=en: A universal Python parser combinator library inspired by Parsec library of Haskell.

Parsec: A parser combinator library in Python
*********************************************

Introduction
============

What's the parsec.py ?

.. automodule:: parsec
    :noindex:

Parser combinator is a technique to implement a parser. A parser combinator is a function (higher-order function)
that accepts several parsers as arguments and return a new parser as result. Parser combinators enable a recursive
descent parsing strategy, this parsing technique facilitates modular piecewise construction and testing. Parser
combinators can be used to combine basic parsers to construct parsers for more complex rules, and parser built
using combinators are straightforward to construct, readable, modular, well-structured and easily maintainable.

`The parsec package <https://hackage.haskell.org/package/parsec>`_ is a famous monadic parser combinator library
in Haskell. Now, the parsec is a parser combinator library implemented in Python, providing Python developers an
easy and elegant approach to build a complex but efficient parser.

Let's go ahead to see the MAGIC of parser combinators!

Examples
========

The design of parsec's API was inspired by Parsec library of Haskell.

Simple parser primitives
-------------------------


For more details about this library, see it's documentation at

.. toctree::
    :maxdepth: 2

    documentation.rst

Usage and Contributor Guide
============================

This project is open-source under `The MIT License <http://mit-license.org>`_ and you may use, distribute and
modify this code with out limitation. The source code can be found at
`the site hosted on github <https://github.com/sighingnow/parsec.py>`_.

* You can install this library using `pip <https://pypi.python.org/pypi/pip>`_ with the following command:

    :code:`pip install parsec`

  or download it from `Pypi <https://pypi.python.org/pypi/parsec>`_ and then install manually.

* Looking for specific information? Try the :doc:`detailed documentation <documentation>`.

* Report bugs with parsec.py in our `Issue tracker <https://github.com/sighingnow/parsec.py/issues>`_.

* Contribute your code to help me improve this library with `Pull Request <https://github.com/sighingnow/parsec.py/pulls>`_.
