# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_setx_and_sety

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.setx(-1023.2334)
    self.nav.sety(193323.234)
    self.assertVectorsAlmostEqual(self.nav.pos(), (-1023.2334, 193323.234))
