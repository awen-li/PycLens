# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_alias_invocation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(aliases=True)
    self.assertEqual(parser.parse_known_args('0.5 1alias1 b'.split()), (NS(foo=False, bar=0.5, w=None, x='b'), []))
    self.assertEqual(parser.parse_known_args('0.5 1alias2 b'.split()), (NS(foo=False, bar=0.5, w=None, x='b'), []))
