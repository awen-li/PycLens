# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vec = Vec2D(0.5, 2)
    self.assertEqual(vec[0], 0.5)
    self.assertEqual(vec[1], 2)
    self.assertIsInstance(vec, Vec2D)
    self.assertRaises(TypeError, Vec2D)
    self.assertRaises(TypeError, Vec2D, 0)
    self.assertRaises(TypeError, Vec2D, (0, 1))
    self.assertRaises(TypeError, Vec2D, vec)
    self.assertRaises(TypeError, Vec2D, 0, 1, 2)
