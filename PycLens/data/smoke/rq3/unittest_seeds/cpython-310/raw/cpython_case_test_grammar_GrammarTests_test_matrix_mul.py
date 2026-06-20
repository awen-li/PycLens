# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_matrix_mul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M:

        def __matmul__(self, o):
            return 4

        def __imatmul__(self, o):
            self.other = o
            return self
    m = M()
    self.assertEqual(m @ m, 4)
    m @= 42
    self.assertEqual(m.other, 42)
