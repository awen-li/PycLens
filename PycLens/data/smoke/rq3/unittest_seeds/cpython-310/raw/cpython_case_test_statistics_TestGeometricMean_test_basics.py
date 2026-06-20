# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestGeometricMean_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    geometric_mean = statistics.geometric_mean
    self.assertAlmostEqual(geometric_mean([54, 24, 36]), 36.0)
    self.assertAlmostEqual(geometric_mean([4.0, 9.0]), 6.0)
    self.assertAlmostEqual(geometric_mean([17.625]), 17.625)
    random.seed(86753095551212)
    for rng in [range(1, 100), range(1, 1000), range(1, 10000), range(500, 10000, 3), range(10000, 500, -3), [12, 17, 13, 5, 120, 7], [random.expovariate(50.0) for i in range(1000)], [random.lognormvariate(20.0, 3.0) for i in range(2000)], [random.triangular(2000, 3000, 2200) for i in range(3000)]]:
        gm_decimal = math.prod(map(Decimal, rng)) ** (Decimal(1) / len(rng))
        gm_float = geometric_mean(rng)
        self.assertTrue(math.isclose(gm_float, float(gm_decimal)))
