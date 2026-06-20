# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_092

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 1
    match x:
        case 0 | (1 | 2):
            y = 0
    self.assertEqual(x, 1)
    self.assertEqual(y, 0)
