# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: ParserTesterMetaclass___init___AddTests_test_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(tester)
    for args_str in tester.failures:
        args = args_str.split()
        with tester.assertRaises(ArgumentParserError, msg=args):
            parser.parse_args(args)
