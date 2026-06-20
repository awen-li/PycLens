# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_139

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = False
    match x:
        case bool(z):
            y = 0
    self.assertIs(x, False)
    self.assertEqual(y, 0)
    self.assertIs(z, x)
