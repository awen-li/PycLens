# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ac_tester.keywords(1, 2), (1, 2))
    self.assertEqual(ac_tester.keywords(1, b=2), (1, 2))
    self.assertEqual(ac_tester.keywords(a=1, b=2), (1, 2))
