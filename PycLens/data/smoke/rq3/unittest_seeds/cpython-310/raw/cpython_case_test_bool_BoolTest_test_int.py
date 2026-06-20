# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int(False), 0)
    self.assertIsNot(int(False), False)
    self.assertEqual(int(True), 1)
    self.assertIsNot(int(True), True)
