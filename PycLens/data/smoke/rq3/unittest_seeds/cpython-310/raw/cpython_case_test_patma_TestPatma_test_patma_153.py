# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_153

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 0
    match ((w := x),):
        case [y as v]:
            z = 0
    self.assertEqual(x, 0)
    self.assertIs(y, x)
    self.assertEqual(z, 0)
    self.assertIs(w, x)
    self.assertIs(v, y)
