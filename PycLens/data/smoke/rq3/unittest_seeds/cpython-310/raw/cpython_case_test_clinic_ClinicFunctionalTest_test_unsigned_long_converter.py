# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_unsigned_long_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import ULONG_MAX
    with self.assertRaises(ValueError):
        ac_tester.unsigned_long_converter(-1)
    with self.assertRaises(OverflowError):
        ac_tester.unsigned_long_converter(ULONG_MAX + 1)
    with self.assertRaises(OverflowError):
        ac_tester.unsigned_long_converter(0, ULONG_MAX + 1)
    with self.assertRaises(TypeError):
        ac_tester.unsigned_long_converter([])
    self.assertEqual(ac_tester.unsigned_long_converter(), (12, 34, 56))
    self.assertEqual(ac_tester.unsigned_long_converter(0, 0, ULONG_MAX + 1), (0, 0, 0))
    self.assertEqual(ac_tester.unsigned_long_converter(0, 0, (ULONG_MAX + 1) * 3 + 123), (0, 0, 123))
