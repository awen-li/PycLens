# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_keywords_kwonly_opt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ac_tester.keywords_kwonly_opt(1), (1, None, None))
    with self.assertRaises(TypeError):
        ac_tester.keywords_kwonly_opt(1, 2)
    self.assertEqual(ac_tester.keywords_kwonly_opt(1, b=2), (1, 2, None))
    self.assertEqual(ac_tester.keywords_kwonly_opt(a=1, c=3), (1, None, 3))
    self.assertEqual(ac_tester.keywords_kwonly_opt(a=1, b=2, c=3), (1, 2, 3))
