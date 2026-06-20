# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(float(False), 0.0)
    self.assertIsNot(float(False), False)
    self.assertEqual(float(True), 1.0)
    self.assertIsNot(float(True), True)
