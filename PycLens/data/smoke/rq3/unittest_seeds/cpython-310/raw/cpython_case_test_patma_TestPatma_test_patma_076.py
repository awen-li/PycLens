# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_076

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'x'
    match x:
        case [b'x']:
            y = 0
        case ['x']:
            y = 1
        case [120]:
            y = 2
        case b'x':
            y = 4
    self.assertEqual(x, b'x')
    self.assertEqual(y, 4)
