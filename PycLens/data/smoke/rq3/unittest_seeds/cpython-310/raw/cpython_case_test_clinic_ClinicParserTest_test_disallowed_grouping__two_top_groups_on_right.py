# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_disallowed_grouping__two_top_groups_on_right

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parse_function_should_fail('\nmodule foo\nfoo.two_top_groups_on_right\n    param: int\n    [\n    group1 : int\n    ]\n    [\n    group2 : int\n    ]\n            ')
