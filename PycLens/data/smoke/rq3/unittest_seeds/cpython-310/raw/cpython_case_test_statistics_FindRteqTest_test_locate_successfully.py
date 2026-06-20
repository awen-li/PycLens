# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FindRteqTest_test_locate_successfully

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (a, l, x, expected_i) in [([1, 1, 1, 2, 3], 0, 1, 2), ([0, 1, 1, 1, 2, 3], 0, 1, 3), ([1, 2, 3, 3, 3], 0, 3, 4)]:
        with self.subTest(a=a, l=l, x=x):
            self.assertEqual(expected_i, statistics._find_rteq(a, l, x))
