# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_home

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.left(30)
    self.nav.forward(-100000)
    self.nav.home()
    self.assertVectorsAlmostEqual(self.nav.pos(), (0, 0))
    self.assertAlmostEqual(self.nav.heading(), 0)
