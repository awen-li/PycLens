# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_constructor_special_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class complex2(complex):
        pass
    for x in (0.0, -0.0, INF, -INF, NAN):
        for y in (0.0, -0.0, INF, -INF, NAN):
            with self.subTest(x=x, y=y):
                z = complex(x, y)
                self.assertFloatsAreIdentical(z.real, x)
                self.assertFloatsAreIdentical(z.imag, y)
                z = complex2(x, y)
                self.assertIs(type(z), complex2)
                self.assertFloatsAreIdentical(z.real, x)
                self.assertFloatsAreIdentical(z.imag, y)
                z = complex(complex2(x, y))
                self.assertIs(type(z), complex)
                self.assertFloatsAreIdentical(z.real, x)
                self.assertFloatsAreIdentical(z.imag, y)
                z = complex2(complex(x, y))
                self.assertIs(type(z), complex2)
                self.assertFloatsAreIdentical(z.real, x)
                self.assertFloatsAreIdentical(z.imag, y)
