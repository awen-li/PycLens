# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_244

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = range(3)
    match x:
        case [*_, y]:
            z = 0
    self.assertEqual(x, range(3))
    self.assertEqual(y, 2)
    self.assertEqual(z, 0)
