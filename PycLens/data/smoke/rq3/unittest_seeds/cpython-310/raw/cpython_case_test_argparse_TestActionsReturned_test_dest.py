# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestActionsReturned_test_dest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    action = parser.add_argument('--foo')
    self.assertEqual(action.dest, 'foo')
    action = parser.add_argument('-b', '--bar')
    self.assertEqual(action.dest, 'bar')
    action = parser.add_argument('-x', '-y')
    self.assertEqual(action.dest, 'x')
