# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g1():
        return

    def g2():
        return 1

    def g3():
        z = [2, 3]
        return (1, *z)
    g1()
    x = g2()
    y = g3()
    self.assertEqual(y, (1, 2, 3), 'unparenthesized star expr return')
    check_syntax_error(self, 'class foo:return 1')
