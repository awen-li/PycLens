# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: ParserTesterMetaclass___init___AddTests_test_successes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(tester)
    for (args, expected_ns) in tester.successes:
        if isinstance(args, str):
            args = args.split()
        result_ns = self._parse_args(parser, args)
        tester.assertEqual(expected_ns, result_ns)
