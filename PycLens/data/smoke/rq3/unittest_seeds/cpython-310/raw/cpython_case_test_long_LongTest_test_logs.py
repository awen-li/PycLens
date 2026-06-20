# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_logs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    LOG10E = math.log10(math.e)
    for exp in list(range(10)) + [100, 1000, 10000]:
        value = 10 ** exp
        log10 = math.log10(value)
        self.assertAlmostEqual(log10, exp)
        expected = exp / LOG10E
        log = math.log(value)
        self.assertAlmostEqual(log, expected)
    for bad in (-(1 << 10000), -2, 0):
        self.assertRaises(ValueError, math.log, bad)
        self.assertRaises(ValueError, math.log10, bad)
