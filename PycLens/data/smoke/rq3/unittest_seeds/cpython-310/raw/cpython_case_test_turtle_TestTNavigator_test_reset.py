# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_reset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.goto(100, -100)
    self.assertAlmostEqual(self.nav.xcor(), 100)
    self.assertAlmostEqual(self.nav.ycor(), -100)
    self.nav.reset()
    self.assertAlmostEqual(self.nav.xcor(), 0)
    self.assertAlmostEqual(self.nav.ycor(), 0)
