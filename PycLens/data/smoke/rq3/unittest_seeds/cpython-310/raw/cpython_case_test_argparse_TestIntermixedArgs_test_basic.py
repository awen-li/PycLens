# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestIntermixedArgs_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo', dest='foo')
    bar = parser.add_argument('--bar', dest='bar', required=True)
    parser.add_argument('cmd')
    parser.add_argument('rest', nargs='*', type=int)
    argv = 'cmd --foo x 1 --bar y 2 3'.split()
    args = parser.parse_intermixed_args(argv)
    self.assertEqual(NS(bar='y', cmd='cmd', foo='x', rest=[1, 2, 3]), args)
    (args, extras) = parser.parse_known_args(argv)
    self.assertEqual(NS(bar='y', cmd='cmd', foo='x', rest=[]), args)
    self.assertEqual(['1', '2', '3'], extras)
    argv = 'cmd --foo x 1 --error 2 --bar y 3'.split()
    (args, extras) = parser.parse_known_intermixed_args(argv)
    self.assertEqual(NS(bar='y', cmd='cmd', foo='x', rest=[1]), args)
    self.assertEqual(['--error', '2', '3'], extras)
    self.assertIsNone(parser.usage)
    self.assertEqual(bar.required, True)
