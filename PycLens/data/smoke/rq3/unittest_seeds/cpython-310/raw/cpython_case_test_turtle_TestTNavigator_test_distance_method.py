# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_distance_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAlmostEqual(self.nav.distance(30, 40), 50)
    vec = Vec2D(0.22, 0.001)
    self.assertAlmostEqual(self.nav.distance(vec), 0.22000227271553355)
    another_turtle = turtle.TNavigator()
    another_turtle.left(90)
    another_turtle.forward(10000)
    self.assertAlmostEqual(self.nav.distance(another_turtle), 10000)
