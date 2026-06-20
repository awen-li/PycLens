# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_previous_round_bugs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(round(562949953421312.5, 1), 562949953421312.5)
    self.assertEqual(round(56294995342131.5, 3), 56294995342131.5)
    self.assertEqual(round(25.0, -1), 20.0)
    self.assertEqual(round(35.0, -1), 40.0)
    self.assertEqual(round(45.0, -1), 40.0)
    self.assertEqual(round(55.0, -1), 60.0)
    self.assertEqual(round(65.0, -1), 60.0)
    self.assertEqual(round(75.0, -1), 80.0)
    self.assertEqual(round(85.0, -1), 80.0)
    self.assertEqual(round(95.0, -1), 100.0)
