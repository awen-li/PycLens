# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_int_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import INT_MIN, INT_MAX
    with self.assertRaises(OverflowError):
        ac_tester.int_converter(INT_MIN - 1)
    with self.assertRaises(OverflowError):
        ac_tester.int_converter(INT_MAX + 1)
    with self.assertRaises(TypeError):
        ac_tester.int_converter(1, 2, 3)
    with self.assertRaises(TypeError):
        ac_tester.int_converter([])
    self.assertEqual(ac_tester.int_converter(), (12, 34, 45))
    self.assertEqual(ac_tester.int_converter(1, 2, '3'), (1, 2, ord('3')))
