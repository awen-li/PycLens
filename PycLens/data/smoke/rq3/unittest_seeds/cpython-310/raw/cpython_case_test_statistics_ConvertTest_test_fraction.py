# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_fraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = statistics._convert(Fraction(95, 99), Fraction)
    self.check_exact_equal(x, Fraction(95, 99))

    class MyFraction(Fraction):

        def __truediv__(self, other):
            return self.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(71, 13), MyFraction)
    self.check_exact_equal(x, MyFraction(71, 13))
