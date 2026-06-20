# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pow.py
# case: PowTest_test_bug705231

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    a = -1.0
    eq(pow(a, 1.23e+167), 1.0)
    eq(pow(a, -1.23e+167), 1.0)
    for b in range(-10, 11):
        eq(pow(a, float(b)), b & 1 and -1.0 or 1.0)
    for n in range(0, 100):
        fiveto = float(5 ** n)
        expected = fiveto % 2.0 and -1.0 or 1.0
        eq(pow(a, fiveto), expected)
        eq(pow(a, -fiveto), expected)
    eq(expected, 1.0)
