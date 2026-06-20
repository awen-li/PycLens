# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_197

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = [Point(-1, 0), Point(1, 2)]
    match w:
        case [Point(x1, y1), Point(x2, y2) as p2]:
            z = 0
    self.assertEqual(w, [Point(-1, 0), Point(1, 2)])
    self.assertIs(x1, w[0].x)
    self.assertIs(y1, w[0].y)
    self.assertIs(p2, w[1])
    self.assertIs(x2, w[1].x)
    self.assertIs(y2, w[1].y)
    self.assertIs(z, 0)
