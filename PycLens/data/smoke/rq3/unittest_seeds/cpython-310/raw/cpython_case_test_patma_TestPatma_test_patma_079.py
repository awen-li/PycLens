# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_079

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 'xxx'
    match x:
        case ['x', 'x', 'x']:
            y = 0
        case ['xxx']:
            y = 1
        case 'xxx':
            y = 2
    self.assertEqual(x, 'xxx')
    self.assertEqual(y, 2)
