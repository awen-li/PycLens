# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FindRteqTest_test_invalid_input_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (a, l, x) in [([1], 2, 1), ([1, 3], 0, 2)]:
        with self.assertRaises(ValueError):
            statistics._find_rteq(a, l, x)
