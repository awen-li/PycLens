# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_long_long_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import LLONG_MIN, LLONG_MAX
    with self.assertRaises(OverflowError):
        ac_tester.long_long_converter(LLONG_MIN - 1)
    with self.assertRaises(OverflowError):
        ac_tester.long_long_converter(LLONG_MAX + 1)
    with self.assertRaises(TypeError):
        ac_tester.long_long_converter([])
    self.assertEqual(ac_tester.long_long_converter(), (12,))
    self.assertEqual(ac_tester.long_long_converter(-1234), (-1234,))
