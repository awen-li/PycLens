# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_yield_in_comprehensions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        [x for x in [(yield 1)]]

    def g():
        [x for x in [(yield from ())]]
    check = self.check_syntax_error
    check('def g(): [(yield x) for x in ()]', "'yield' inside list comprehension")
    check('def g(): [x for x in () if not (yield x)]', "'yield' inside list comprehension")
    check('def g(): [y for x in () for y in [(yield x)]]', "'yield' inside list comprehension")
    check('def g(): {(yield x) for x in ()}', "'yield' inside set comprehension")
    check('def g(): {(yield x): x for x in ()}', "'yield' inside dict comprehension")
    check('def g(): {x: (yield x) for x in ()}', "'yield' inside dict comprehension")
    check('def g(): ((yield x) for x in ())', "'yield' inside generator expression")
    check('def g(): [(yield from x) for x in ()]', "'yield' inside list comprehension")
    check('class C: [(yield x) for x in ()]', "'yield' inside list comprehension")
    check('[(yield x) for x in ()]', "'yield' inside list comprehension")
