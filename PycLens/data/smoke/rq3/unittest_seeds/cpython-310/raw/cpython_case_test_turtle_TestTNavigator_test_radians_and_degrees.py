# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_radians_and_degrees

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.left(90)
    self.assertAlmostEqual(self.nav.heading(), 90)
    self.nav.radians()
    self.assertAlmostEqual(self.nav.heading(), 1.57079633)
    self.nav.degrees()
    self.assertAlmostEqual(self.nav.heading(), 90)
