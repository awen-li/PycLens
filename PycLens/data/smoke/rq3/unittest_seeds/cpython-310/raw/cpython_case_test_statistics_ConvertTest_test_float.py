# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = statistics._convert(Fraction(-1, 2), float)
    self.check_exact_equal(x, -0.5)

    class MyFloat(float):

        def __truediv__(self, other):
            return self.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(9, 8), MyFloat)
    self.check_exact_equal(x, MyFloat(1.125))
