# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExpandDefaults_test_default_none_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-f', '--file', help=self.file_help)
    self.parser.set_defaults(file=None)
    self.assertHelp(self.parser, self.expected_help_none)
