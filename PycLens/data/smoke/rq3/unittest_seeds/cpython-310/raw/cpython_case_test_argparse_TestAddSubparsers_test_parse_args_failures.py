# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_parse_args_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for args_str in ['', 'a', 'a a', '0.5 a', '0.5 1', '0.5 1 -y', '0.5 2 -w']:
        args = args_str.split()
        self.assertArgumentParserError(self.parser.parse_args, args)
