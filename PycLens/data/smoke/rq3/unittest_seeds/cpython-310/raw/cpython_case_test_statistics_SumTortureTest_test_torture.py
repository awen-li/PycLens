# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: SumTortureTest_test_torture

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(statistics._sum([1, 1e+100, 1, -1e+100] * 10000), (float, Fraction(20000.0), 40000))
    self.assertEqual(statistics._sum([1e+100, 1, 1, -1e+100] * 10000), (float, Fraction(20000.0), 40000))
    (T, num, count) = statistics._sum([1e-100, 1, 1e-100, -1] * 10000)
    self.assertIs(T, float)
    self.assertEqual(count, 40000)
    self.assertApproxEqual(float(num), 2e-96, rel=5e-16)
