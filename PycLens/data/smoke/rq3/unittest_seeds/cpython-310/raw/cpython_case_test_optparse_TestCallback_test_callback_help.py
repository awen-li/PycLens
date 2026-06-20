# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallback_test_callback_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = OptionParser(usage=SUPPRESS_USAGE)
    parser.remove_option('-h')
    parser.add_option('-t', '--test', action='callback', callback=lambda : None, type='string', help='foo')
    expected_help = 'Options:\n  -t TEST, --test=TEST  foo\n'
    self.assertHelp(parser, expected_help)
