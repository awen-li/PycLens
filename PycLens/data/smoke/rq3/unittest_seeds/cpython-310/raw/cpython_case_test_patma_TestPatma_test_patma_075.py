# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_075

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 'x'
    match x:
        case ['x']:
            y = 0
        case 'x':
            y = 1
    self.assertEqual(x, 'x')
    self.assertEqual(y, 1)
