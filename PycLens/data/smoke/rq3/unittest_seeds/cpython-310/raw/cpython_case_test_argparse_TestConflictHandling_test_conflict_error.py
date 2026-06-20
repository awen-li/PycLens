# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestConflictHandling_test_conflict_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    self.assertRaises(argparse.ArgumentError, parser.add_argument, '-x')
    parser.add_argument('--spam')
    self.assertRaises(argparse.ArgumentError, parser.add_argument, '--spam')
