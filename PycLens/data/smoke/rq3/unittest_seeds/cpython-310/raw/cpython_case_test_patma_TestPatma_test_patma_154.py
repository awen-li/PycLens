# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_154

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 0
    y = None
    match x:
        case 0 if x:
            y = 0
    self.assertEqual(x, 0)
    self.assertIs(y, None)
