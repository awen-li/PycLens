# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_posonly_keywords_opt_kwonly_opt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_opt_kwonly_opt(1)
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2), (1, 2, None, None, None))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, b=2), (1, 2, None, None, None))
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, 3, 4)
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_opt_kwonly_opt(a=1, b=2)
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, c=3), (1, 2, 3, None, None))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, b=2, c=3), (1, 2, 3, None, None))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, 3, d=4), (1, 2, 3, 4, None))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, c=3, d=4), (1, 2, 3, 4, None))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, 3, d=4, e=5), (1, 2, 3, 4, 5))
    self.assertEqual(ac_tester.posonly_keywords_opt_kwonly_opt(1, 2, c=3, d=4, e=5), (1, 2, 3, 4, 5))
