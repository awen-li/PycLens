# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_142

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b''
    match x:
        case bytes(z):
            y = 0
    self.assertEqual(x, b'')
    self.assertEqual(y, 0)
    self.assertIs(z, x)
