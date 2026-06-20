# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_keyword_only_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.keyword_only_parameter()
    with self.assertRaises(TypeError):
        ac_tester.keyword_only_parameter(1)
    self.assertEqual(ac_tester.keyword_only_parameter(a=1), (1,))
