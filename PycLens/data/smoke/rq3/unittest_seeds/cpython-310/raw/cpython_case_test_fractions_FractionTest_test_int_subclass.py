# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fractions.py
# case: FractionTest_test_int_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class myint(int):

        def __mul__(self, other):
            return type(self)(int(self) * int(other))

        def __floordiv__(self, other):
            return type(self)(int(self) // int(other))

        def __mod__(self, other):
            x = type(self)(int(self) % int(other))
            return x

        @property
        def numerator(self):
            return type(self)(int(self))

        @property
        def denominator(self):
            return type(self)(1)
    f = fractions.Fraction(myint(1 * 3), myint(2 * 3))
    self.assertEqual(f.numerator, 1)
    self.assertEqual(f.denominator, 2)
    self.assertEqual(type(f.numerator), myint)
    self.assertEqual(type(f.denominator), myint)
