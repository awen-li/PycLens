# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExpandDefaults_test_no_expand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-f', '--file', default='foo.txt', help='read from %default file')
    self.parser.formatter.default_tag = None
    expected_help = self.help_prefix + '  -f FILE, --file=FILE  read from %default file\n'
    self.assertHelp(self.parser, expected_help)
