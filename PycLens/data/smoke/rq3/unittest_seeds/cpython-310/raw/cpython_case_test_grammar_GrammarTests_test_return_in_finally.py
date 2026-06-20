# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_return_in_finally

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g1():
        try:
            pass
        finally:
            return 1
    self.assertEqual(g1(), 1)

    def g2():
        try:
            return 2
        finally:
            return 3
    self.assertEqual(g2(), 3)

    def g3():
        try:
            1 / 0
        finally:
            return 4
    self.assertEqual(g3(), 4)
