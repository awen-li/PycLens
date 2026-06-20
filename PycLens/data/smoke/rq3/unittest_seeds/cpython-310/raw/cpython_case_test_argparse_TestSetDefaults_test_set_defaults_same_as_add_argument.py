# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_same_as_add_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.set_defaults(w='W', x='X', y='Y', z='Z')
    parser.add_argument('-w')
    parser.add_argument('-x', default='XX')
    parser.add_argument('y', nargs='?')
    parser.add_argument('z', nargs='?', default='ZZ')
    self.assertEqual(NS(w='W', x='XX', y='Y', z='ZZ'), parser.parse_args([]))
    parser.set_defaults(w='WW', x='X', y='YY', z='Z')
    self.assertEqual(NS(w='WW', x='X', y='YY', z='Z'), parser.parse_args([]))
