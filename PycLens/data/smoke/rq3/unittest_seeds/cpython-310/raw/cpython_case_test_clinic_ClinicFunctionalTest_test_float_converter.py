# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_float_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.float_converter([])
    self.assertEqual(ac_tester.float_converter(), (12.5,))
    self.assertEqual(ac_tester.float_converter(-0.5), (-0.5,))
