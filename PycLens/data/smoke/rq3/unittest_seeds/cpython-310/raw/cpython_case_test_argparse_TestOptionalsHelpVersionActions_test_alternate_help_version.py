# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_alternate_help_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.add_argument('-x', action='help')
    parser.add_argument('-y', action='version')
    self.assertPrintHelpExit(parser, '-x')
    self.assertArgumentParserError(parser, '-v')
    self.assertArgumentParserError(parser, '--version')
    self.assertRaises(AttributeError, getattr, parser, 'format_version')
