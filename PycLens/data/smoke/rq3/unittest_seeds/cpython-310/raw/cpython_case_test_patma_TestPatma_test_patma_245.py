# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_245

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {'y': 1}
    match x:
        case {'y': (0 as y) | (1 as y)}:
            z = 0
    self.assertEqual(x, {'y': 1})
    self.assertEqual(y, 1)
    self.assertEqual(z, 0)
