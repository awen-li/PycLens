# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_decimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = statistics._convert(Fraction(1, 40), Decimal)
    self.check_exact_equal(x, Decimal('0.025'))

    class MyDecimal(Decimal):

        def __truediv__(self, other):
            return self.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(-15, 16), MyDecimal)
    self.check_exact_equal(x, MyDecimal('-0.9375'))
