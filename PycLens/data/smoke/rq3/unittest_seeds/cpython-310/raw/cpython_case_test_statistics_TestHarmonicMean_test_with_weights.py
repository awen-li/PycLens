# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_with_weights

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.func([40, 60], [5, 30]), 56.0)
    self.assertEqual(self.func([40, 60], weights=[5, 30]), 56.0)
    self.assertEqual(self.func(iter([40, 60]), iter([5, 30])), 56.0)
    self.assertEqual(self.func([Fraction(10, 3), Fraction(23, 5), Fraction(7, 2)], [5, 2, 10]), self.func([Fraction(10, 3)] * 5 + [Fraction(23, 5)] * 2 + [Fraction(7, 2)] * 10))
    self.assertEqual(self.func([10], [7]), 10)
    with self.assertRaises(TypeError):
        self.func([1, 2, 3], [1, (), 3])
    with self.assertRaises(statistics.StatisticsError):
        self.func([1, 2, 3], [1, 2])
    with self.assertRaises(statistics.StatisticsError):
        self.func([10], [0])
    with self.assertRaises(statistics.StatisticsError):
        self.func([10, 20], [0, 0])
