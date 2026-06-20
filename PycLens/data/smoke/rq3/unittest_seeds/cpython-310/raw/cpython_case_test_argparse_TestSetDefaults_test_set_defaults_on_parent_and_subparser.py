# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestSetDefaults_test_set_defaults_on_parent_and_subparser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    xparser = parser.add_subparsers().add_parser('X')
    parser.set_defaults(foo=1)
    xparser.set_defaults(foo=2)
    self.assertEqual(NS(foo=2), parser.parse_args(['X']))
