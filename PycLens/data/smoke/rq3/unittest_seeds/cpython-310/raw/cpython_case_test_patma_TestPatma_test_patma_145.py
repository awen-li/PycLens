# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_145

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = frozenset()
    match x:
        case frozenset(z):
            y = 0
    self.assertEqual(x, frozenset())
    self.assertEqual(y, 0)
    self.assertIs(z, x)
