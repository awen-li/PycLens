# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestOptimizedCompares_test_not_all_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, [(1.0, 1.0), (False, 'A'), 6].sort)
    self.assertRaises(TypeError, [('a', 1), (1, 'a')].sort)
    self.assertRaises(TypeError, [(1, 'a'), ('a', 1)].sort)
