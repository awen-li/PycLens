# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_backwards

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.back(200)
    expected = Vec2D(-200, 0)
    self.assertVectorsAlmostEqual(self.nav.position(), expected)
    self.nav.reset()
    self.nav.right(90)
    self.nav.back(200)
    expected = Vec2D(0, 200)
    self.assertVectorsAlmostEqual(self.nav.position(), expected)
