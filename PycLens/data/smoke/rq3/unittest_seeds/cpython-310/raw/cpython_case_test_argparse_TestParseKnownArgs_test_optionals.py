# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParseKnownArgs_test_optionals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    (args, extras) = parser.parse_known_args('--foo F --bar --baz'.split())
    self.assertEqual(NS(foo='F'), args)
    self.assertEqual(['--bar', '--baz'], extras)
