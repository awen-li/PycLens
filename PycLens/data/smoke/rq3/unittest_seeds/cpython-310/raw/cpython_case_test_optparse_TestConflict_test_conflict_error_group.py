# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflict_test_conflict_error_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    group = OptionGroup(self.parser, 'Group 1')
    self.assertTrueconflict_error(group.add_option)
