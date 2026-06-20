# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_forward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.forward(150)
    expected = Vec2D(150, 0)
    self.assertVectorsAlmostEqual(self.nav.position(), expected)
    self.nav.reset()
    self.nav.left(90)
    self.nav.forward(150)
    expected = Vec2D(0, 150)
    self.assertVectorsAlmostEqual(self.nav.position(), expected)
    self.assertRaises(TypeError, self.nav.forward, 'skldjfldsk')
