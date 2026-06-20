# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_repeated_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (7.2, 49, 8100000000000000.0, Fraction(3, 7), Decimal('62.4802')):
        for count in (2, 3, 5, 15):
            data = [x] * count
            self.assertEqual(self.func(data), 0)
