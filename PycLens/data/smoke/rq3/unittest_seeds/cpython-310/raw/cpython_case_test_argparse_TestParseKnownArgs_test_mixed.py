# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParseKnownArgs_test_mixed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', nargs='?', const=1, type=int)
    parser.add_argument('--spam', action='store_false')
    parser.add_argument('badger')
    argv = ['B', 'C', '--foo', '-v', '3', '4']
    (args, extras) = parser.parse_known_args(argv)
    self.assertEqual(NS(v=3, spam=True, badger='B'), args)
    self.assertEqual(['C', '--foo', '4'], extras)
