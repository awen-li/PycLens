# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FindLteqTest_test_invalid_input_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (a, x) in [([], 1), ([1, 2], 3), ([1, 3], 2)]:
        with self.subTest(a=a, x=x):
            with self.assertRaises(ValueError):
                statistics._find_lteq(a, x)
