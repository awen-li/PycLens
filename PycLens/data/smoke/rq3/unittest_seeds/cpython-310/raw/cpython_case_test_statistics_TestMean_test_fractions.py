# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    F = Fraction
    data = [F(1, 2), F(2, 3), F(3, 4), F(4, 5), F(5, 6), F(6, 7), F(7, 8)]
    random.shuffle(data)
    self.assertEqual(self.func(data), F(1479, 1960))
