# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_disallowed_grouping__empty_group_on_right

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parse_function_should_fail('\nmodule foo\nfoo.empty_group\n    param: int\n    [\n    [\n    ]\n    group2 : int\n    ]\n            ')
