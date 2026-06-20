# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExpandDefaults_test_alt_expand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-f', '--file', default='foo.txt', help='read from FILE [default: *DEFAULT*]')
    self.parser.formatter.default_tag = '*DEFAULT*'
    self.assertHelp(self.parser, self.expected_help_file)
