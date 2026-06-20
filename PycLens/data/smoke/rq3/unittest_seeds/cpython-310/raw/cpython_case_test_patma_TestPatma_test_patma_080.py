# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_080

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'xxx'
    match x:
        case [120, 120, 120]:
            y = 0
        case [b'xxx']:
            y = 1
        case b'xxx':
            y = 2
    self.assertEqual(x, b'xxx')
    self.assertEqual(y, 2)
