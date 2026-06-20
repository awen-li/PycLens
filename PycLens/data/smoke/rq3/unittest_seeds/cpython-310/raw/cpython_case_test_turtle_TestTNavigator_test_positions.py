# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_positions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.forward(100)
    self.nav.left(90)
    self.nav.forward(-200)
    self.assertVectorsAlmostEqual(self.nav.pos(), (100.0, -200.0))
