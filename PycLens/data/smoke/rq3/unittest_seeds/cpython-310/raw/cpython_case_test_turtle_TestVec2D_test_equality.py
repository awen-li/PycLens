# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestVec2D_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vec1 = Vec2D(0, 1)
    vec2 = Vec2D(0.0, 1)
    vec3 = Vec2D(42, 1)
    self.assertEqual(vec1, vec2)
    self.assertEqual(vec1, tuple(vec1))
    self.assertEqual(tuple(vec1), vec1)
    self.assertNotEqual(vec1, vec3)
    self.assertNotEqual(vec2, vec3)
