# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_gh_99240_double_free

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_error = 'gh_99240_double_free\\(\\) argument 2 must be encoded string without null bytes, not str'
    with self.assertRaisesRegex(TypeError, expected_error):
        ac_tester.gh_99240_double_free('a', '\x00b')
