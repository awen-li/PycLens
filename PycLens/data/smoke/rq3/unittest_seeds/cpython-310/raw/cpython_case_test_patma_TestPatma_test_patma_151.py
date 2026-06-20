# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_151

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 0
    match (x,):
        case [y]:
            z = 0
    self.assertEqual(x, 0)
    self.assertIs(y, x)
    self.assertIs(z, 0)
