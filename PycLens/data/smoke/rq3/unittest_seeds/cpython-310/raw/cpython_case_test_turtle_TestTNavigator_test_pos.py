# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_pos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.nav.pos(), self.nav._position)
    self.nav.goto(100, -100)
    self.assertEqual(self.nav.pos(), self.nav._position)
