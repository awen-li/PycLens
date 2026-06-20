# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_version_no_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(add_help=False)
    parser.add_argument('-v', '--version', action='version', version='1.0')
    self.assertArgumentParserError(parser, '-h')
    self.assertArgumentParserError(parser, '--help')
    self.assertRaises(AttributeError, getattr, parser, 'format_version')
