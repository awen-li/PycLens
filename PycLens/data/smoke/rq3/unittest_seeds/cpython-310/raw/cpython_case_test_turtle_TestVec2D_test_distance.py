# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_distance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAlmostEqual(abs(Vec2D(6, 8)), 10)
    self.assertEqual(abs(Vec2D(0, 0)), 0)
    self.assertAlmostEqual(abs(Vec2D(2.5, 6)), 6.5)
