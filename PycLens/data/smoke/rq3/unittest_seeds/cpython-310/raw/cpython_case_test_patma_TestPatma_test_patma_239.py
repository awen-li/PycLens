# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_239

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = collections.UserDict({0: 1, 2: 3})
    match x:
        case {2: 3}:
            y = 0
    self.assertEqual(x, {0: 1, 2: 3})
    self.assertEqual(y, 0)
