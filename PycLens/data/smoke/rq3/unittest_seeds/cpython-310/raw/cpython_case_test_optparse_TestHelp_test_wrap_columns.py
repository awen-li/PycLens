# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestHelp_test_wrap_columns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser = self.make_parser(60)
    self.assertHelpEquals(_expected_help_short_lines)
    self.parser = self.make_parser(0)
    self.assertHelpEquals(_expected_very_help_short_lines)
