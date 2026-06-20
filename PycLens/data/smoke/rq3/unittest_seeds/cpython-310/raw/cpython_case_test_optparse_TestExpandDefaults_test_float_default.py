# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExpandDefaults_test_float_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.add_option('-p', '--prob', help='blow up with probability PROB [default: %default]')
    self.parser.set_defaults(prob=0.43)
    expected_help = self.help_prefix + '  -p PROB, --prob=PROB  blow up with probability PROB [default: 0.43]\n'
    self.assertHelp(self.parser, expected_help)
