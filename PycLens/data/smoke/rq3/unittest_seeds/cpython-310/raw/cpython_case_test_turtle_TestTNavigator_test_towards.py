# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_towards

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    coordinates = [((100, 0), 0.0), ((100, 100), 45.0), ((0, 100), 90.0), ((-100, 100), 135.0), ((-100, 0), 180.0), ((-100, -100), 225.0), ((0, -100), 270.0), ((100, -100), 315.0)]
    for ((x, y), expected) in coordinates:
        self.assertEqual(self.nav.towards(x, y), expected)
        self.assertEqual(self.nav.towards((x, y)), expected)
        self.assertEqual(self.nav.towards(Vec2D(x, y)), expected)
