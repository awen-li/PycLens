# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_with_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo', y='bar')
    parser.add_argument('-x', default='xfoox')
    self.assertEqual(NS(x='xfoox', y='bar'), parser.parse_args([]))
    self.assertEqual(NS(x='xfoox', y='bar'), parser.parse_args([], NS()))
    self.assertEqual(NS(x='baz', y='bar'), parser.parse_args([], NS(x='baz')))
    self.assertEqual(NS(x='1', y='bar'), parser.parse_args('-x 1'.split()))
    self.assertEqual(NS(x='1', y='bar'), parser.parse_args('-x 1'.split(), NS()))
    self.assertEqual(NS(x='1', y='bar'), parser.parse_args('-x 1'.split(), NS(x='baz')))
