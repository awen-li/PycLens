# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_disallowed_grouping__two_top_groups_on_left

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.parse_function_should_fail('\nmodule foo\nfoo.two_top_groups_on_left\n    [\n    group1 : int\n    ]\n    [\n    group2 : int\n    ]\n    param: int\n            ')
    self.assertEqual(s, 'Error on line 0:\nFunction two_top_groups_on_left has an unsupported group configuration. (Unexpected state 2.b)\n')
