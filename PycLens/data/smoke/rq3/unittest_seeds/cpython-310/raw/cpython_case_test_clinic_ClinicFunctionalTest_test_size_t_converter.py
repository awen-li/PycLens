# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_size_t_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        ac_tester.size_t_converter(-1)
    with self.assertRaises(TypeError):
        ac_tester.size_t_converter([])
    self.assertEqual(ac_tester.size_t_converter(), (12,))
