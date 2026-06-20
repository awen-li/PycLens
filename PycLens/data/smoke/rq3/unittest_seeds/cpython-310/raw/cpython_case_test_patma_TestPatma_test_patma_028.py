# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_028

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {0: 3}
    y = None
    match x:
        case {0: 0 | 1 | 2 as z}:
            y = 0
    self.assertEqual(x, {0: 3})
    self.assertIs(y, None)
