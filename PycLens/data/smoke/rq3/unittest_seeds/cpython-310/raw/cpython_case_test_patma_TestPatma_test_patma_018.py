# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_018

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    match (0, 1, 2):
        case [0, *x, 2]:
            y = 0
    self.assertEqual(x, [1])
    self.assertEqual(y, 0)
