# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_no_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(add_help=False)
    self.assertArgumentParserError(parser, '-h')
    self.assertArgumentParserError(parser, '--help')
    self.assertArgumentParserError(parser, '-v')
    self.assertArgumentParserError(parser, '--version')
