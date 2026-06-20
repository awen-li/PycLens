# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_setheading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.setheading(102.32)
    self.assertAlmostEqual(self.nav.heading(), 102.32)
    self.nav.setheading(-123.23)
    self.assertAlmostEqual(self.nav.heading(), -123.23 % 360)
    self.nav.setheading(-1000.34)
    self.assertAlmostEqual(self.nav.heading(), -1000.34 % 360)
    self.nav.setheading(300000)
    self.assertAlmostEqual(self.nav.heading(), 300000 % 360)
