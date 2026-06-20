# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicGroupPermuterTest_test_have_left_options_but_required_is_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fn():
        clinic.permute_optional_groups(['a'], [], [])
    self.assertRaises(AssertionError, fn)
