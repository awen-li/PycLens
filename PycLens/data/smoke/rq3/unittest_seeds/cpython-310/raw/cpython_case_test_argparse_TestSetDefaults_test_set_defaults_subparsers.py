# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_subparsers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo')
    subparsers = parser.add_subparsers()
    parser_a = subparsers.add_parser('a')
    parser_a.set_defaults(y='bar')
    self.assertEqual(NS(x='foo', y='bar'), parser.parse_args('a'.split()))
