# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_real_and_imag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True .real, 1)
    self.assertEqual(True .imag, 0)
    self.assertIs(type(True .real), int)
    self.assertIs(type(True .imag), int)
    self.assertEqual(False .real, 0)
    self.assertEqual(False .imag, 0)
    self.assertIs(type(False .real), int)
    self.assertIs(type(False .imag), int)
