# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(statistics._exact_ratio(0.125), (1, 8))
    self.assertEqual(statistics._exact_ratio(1.125), (9, 8))
    data = [random.uniform(-100, 100) for _ in range(100)]
    for x in data:
        (num, den) = statistics._exact_ratio(x)
        self.assertEqual(x, num / den)
