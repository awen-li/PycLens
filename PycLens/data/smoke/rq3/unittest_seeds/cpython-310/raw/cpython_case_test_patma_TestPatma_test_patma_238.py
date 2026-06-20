# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_238

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ((0, 1), (2, 3))
    match x:
        case [([a as b, c as d] as e) as w, ([f as g, h] as i) as z]:
            y = 0
    self.assertEqual(a, 0)
    self.assertEqual(b, 0)
    self.assertEqual(c, 1)
    self.assertEqual(d, 1)
    self.assertEqual(e, (0, 1))
    self.assertEqual(f, 2)
    self.assertEqual(g, 2)
    self.assertEqual(h, 3)
    self.assertEqual(i, (2, 3))
    self.assertEqual(w, (0, 1))
    self.assertEqual(x, ((0, 1), (2, 3)))
    self.assertEqual(y, 0)
    self.assertEqual(z, (2, 3))
