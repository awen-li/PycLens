# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_dest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.add_argument('--foo', action='store_true')
    subparsers = parser.add_subparsers(dest='bar')
    parser1 = subparsers.add_parser('1')
    parser1.add_argument('baz')
    self.assertEqual(NS(foo=False, bar='1', baz='2'), parser.parse_args('1 2'.split()))
