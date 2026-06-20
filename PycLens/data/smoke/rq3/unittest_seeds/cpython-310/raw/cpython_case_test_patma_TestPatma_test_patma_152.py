# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_152

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = 0
    x = 0
    match (w, x):
        case [y, z]:
            v = 0
    self.assertEqual(w, 0)
    self.assertEqual(x, 0)
    self.assertIs(y, w)
    self.assertIs(z, x)
    self.assertEqual(v, 0)
