# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_no_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo')
    parser.set_defaults(y='bar', z=1)
    self.assertEqual(NS(x='foo', y='bar', z=1), parser.parse_args([]))
    self.assertEqual(NS(x='foo', y='bar', z=1), parser.parse_args([], NS()))
    self.assertEqual(NS(x='baz', y='bar', z=1), parser.parse_args([], NS(x='baz')))
    self.assertEqual(NS(x='baz', y='bar', z=2), parser.parse_args([], NS(x='baz', z=2)))
