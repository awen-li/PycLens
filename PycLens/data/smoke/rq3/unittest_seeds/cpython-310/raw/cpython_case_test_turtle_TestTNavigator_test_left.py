# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_left

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.nav._orient, (1.0, 0))
    self.nav.left(90)
    self.assertVectorsAlmostEqual(self.nav._orient, (0.0, 1.0))
