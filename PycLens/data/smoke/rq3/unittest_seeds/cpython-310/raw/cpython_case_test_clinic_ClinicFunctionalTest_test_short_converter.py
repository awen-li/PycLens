# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_short_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import SHRT_MIN, SHRT_MAX
    with self.assertRaises(OverflowError):
        ac_tester.short_converter(SHRT_MIN - 1)
    with self.assertRaises(OverflowError):
        ac_tester.short_converter(SHRT_MAX + 1)
    with self.assertRaises(TypeError):
        ac_tester.short_converter([])
    self.assertEqual(ac_tester.short_converter(-1234), (-1234,))
    self.assertEqual(ac_tester.short_converter(4321), (4321,))
