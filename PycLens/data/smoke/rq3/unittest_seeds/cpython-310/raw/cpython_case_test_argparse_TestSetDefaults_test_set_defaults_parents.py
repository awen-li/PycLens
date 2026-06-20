# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parent = ErrorRaisingArgumentParser(add_help=False)
    parent.set_defaults(x='foo')
    parser = ErrorRaisingArgumentParser(parents=[parent])
    self.assertEqual(NS(x='foo'), parser.parse_args([]))
