# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in (-20, -3, 0, 5, 99, 10 ** 20):
        self.assertEqual(statistics._exact_ratio(i), (i, 1))
