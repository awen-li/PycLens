# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='1.0')
    self.assertPrintHelpExit(parser, '-h')
    self.assertPrintHelpExit(parser, '--help')
    self.assertRaises(AttributeError, getattr, parser, 'format_version')
