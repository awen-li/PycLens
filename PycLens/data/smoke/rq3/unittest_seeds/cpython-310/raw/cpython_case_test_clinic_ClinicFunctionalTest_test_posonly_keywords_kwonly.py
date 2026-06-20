# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_posonly_keywords_kwonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_kwonly(1)
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_kwonly(1, 2, 3)
    with self.assertRaises(TypeError):
        ac_tester.posonly_keywords_kwonly(a=1, b=2, c=3)
    self.assertEqual(ac_tester.posonly_keywords_kwonly(1, 2, c=3), (1, 2, 3))
    self.assertEqual(ac_tester.posonly_keywords_kwonly(1, b=2, c=3), (1, 2, 3))
