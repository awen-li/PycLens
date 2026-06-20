# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_disallowed_grouping__group_after_parameter_on_left

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parse_function_should_fail('\nmodule foo\nfoo.group_after_parameter_on_left\n    [\n    group2 : int\n    [\n    group1 : int\n    ]\n    ]\n    param: int\n            ')
