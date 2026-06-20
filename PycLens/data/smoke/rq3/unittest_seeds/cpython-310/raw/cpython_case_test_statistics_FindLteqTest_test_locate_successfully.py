# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FindLteqTest_test_locate_successfully

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (a, x, expected_i) in [([1, 1, 1, 2, 3], 1, 0), ([0, 1, 1, 1, 2, 3], 1, 1), ([1, 2, 3, 3, 3], 3, 2)]:
        with self.subTest(a=a, x=x):
            self.assertEqual(expected_i, statistics._find_lteq(a, x))
