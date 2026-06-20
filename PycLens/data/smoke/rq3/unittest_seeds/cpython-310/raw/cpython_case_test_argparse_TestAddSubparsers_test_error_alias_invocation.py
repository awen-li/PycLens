# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_error_alias_invocation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(aliases=True)
    self.assertArgumentParserError(parser.parse_args, '0.5 1alias3 b'.split())
