# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_077

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = bytearray(b'x')
    y = None
    match x:
        case [120]:
            y = 0
        case 120:
            y = 1
    self.assertEqual(x, b'x')
    self.assertIs(y, None)
