# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_conflicting_parents_mutex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(argparse.ArgumentError, argparse.ArgumentParser, parents=[self.abcd_parent, self.ab_mutex_parent])
