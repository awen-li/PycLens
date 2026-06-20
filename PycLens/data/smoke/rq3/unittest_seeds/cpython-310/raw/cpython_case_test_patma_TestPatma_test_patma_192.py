# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_192

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = range(1 << 30)
    match w:
        case [x, y, *_]:
            z = 0
    self.assertEqual(w, range(1 << 30))
    self.assertEqual(x, 0)
    self.assertEqual(y, 1)
    self.assertEqual(z, 0)
