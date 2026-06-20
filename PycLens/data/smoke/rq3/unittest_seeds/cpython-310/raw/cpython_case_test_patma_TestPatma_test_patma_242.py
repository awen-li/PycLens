# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_242

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = range(3)
    match x:
        case [y, *_, z]:
            w = 0
    self.assertEqual(w, 0)
    self.assertEqual(x, range(3))
    self.assertEqual(y, 0)
    self.assertEqual(z, 2)
