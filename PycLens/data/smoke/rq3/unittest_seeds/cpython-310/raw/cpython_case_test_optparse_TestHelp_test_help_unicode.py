# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestHelp_test_help_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
    self.parser.add_option('-a', action='store_true', help='olé!')
    expect = 'Options:\n  -h, --help  show this help message and exit\n  -a          olé!\n'
    self.assertHelpEquals(expect)
