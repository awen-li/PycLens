# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_189

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = range(1000)
    match w:
        case [x, y, *rest]:
            z = 0
    self.assertEqual(w, range(1000))
    self.assertEqual(x, 0)
    self.assertEqual(y, 1)
    self.assertEqual(z, 0)
    self.assertEqual(rest, list(range(2, 1000)))
