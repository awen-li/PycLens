# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_yield

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        yield 1

    def g():
        yield from ()

    def g():
        x = (yield 1)

    def g():
        x = (yield from ())

    def g():
        yield (1, 1)

    def g():
        x = (yield (1, 1))
    check_syntax_error(self, 'def g(): yield from (), 1')
    check_syntax_error(self, 'def g(): x = yield from (), 1')

    def g():
        (1, (yield 1))

    def g():
        (1, (yield from ()))
    check_syntax_error(self, 'def g(): 1, yield 1')
    check_syntax_error(self, 'def g(): 1, yield from ()')

    def g():
        f((yield 1))

    def g():
        f((yield 1), 1)

    def g():
        f((yield from ()))

    def g():
        f((yield from ()), 1)

    def g():
        rest = (4, 5, 6)
        yield (1, 2, 3, *rest)
    self.assertEqual(list(g()), [(1, 2, 3, 4, 5, 6)])
    check_syntax_error(self, 'def g(): f(yield 1)')
    check_syntax_error(self, 'def g(): f(yield 1, 1)')
    check_syntax_error(self, 'def g(): f(yield from ())')
    check_syntax_error(self, 'def g(): f(yield from (), 1)')
    check_syntax_error(self, 'yield')
    check_syntax_error(self, 'yield from')
    check_syntax_error(self, 'class foo:yield 1')
    check_syntax_error(self, 'class foo:yield from ()')
    check_syntax_error(self, 'def g(a:(yield)): pass')
