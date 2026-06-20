# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_repeated_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (5.3, 68, 4.3e+17, Fraction(29, 101), Decimal('32.9714')):
        for count in (2, 5, 10, 20):
            data = [x] * count
            self.assertEqual(self.func(data), float(x))
