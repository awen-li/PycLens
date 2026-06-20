# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xxlimited.py
# case: CommonTests_test_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(self.module.Str, str))
    self.assertIsNot(self.module.Str, str)
    custom_string = self.module.Str('abcd')
    self.assertEqual(custom_string, 'abcd')
    self.assertEqual(custom_string.upper(), 'ABCD')
