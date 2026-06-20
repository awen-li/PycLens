# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_regression_25177

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(statistics.mean([8.988465674311579e+307, 8.98846567431158e+307]), 8.98846567431158e+307)
    big = 8.98846567431158e+307
    tiny = 5e-324
    for n in (2, 3, 5, 200):
        self.assertEqual(statistics.mean([big] * n), big)
        self.assertEqual(statistics.mean([tiny] * n), tiny)
