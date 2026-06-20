# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_internal_use_of_overridden_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal

    class X(float):

        def as_integer_ratio(self):
            return 1

        def __abs__(self):
            return self

    class Y(float):

        def __abs__(self):
            return [1] * 200

    class I(int):

        def bit_length(self):
            return [1] * 200

    class Z(float):

        def as_integer_ratio(self):
            return (I(1), I(1))

        def __abs__(self):
            return self
    for cls in (X, Y, Z):
        self.assertEqual(Decimal.from_float(cls(101.1)), Decimal.from_float(101.1))
