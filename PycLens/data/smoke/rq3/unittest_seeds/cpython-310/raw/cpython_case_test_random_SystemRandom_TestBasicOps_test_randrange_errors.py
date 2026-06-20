# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_randrange_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raises = partial(self.assertRaises, ValueError, self.gen.randrange)
    raises(3, 3)
    raises(-721)
    raises(0, 100, -12)
    self.assertWarns(DeprecationWarning, raises, 3.14159)
    self.assertWarns(DeprecationWarning, self.gen.randrange, 3.0)
    self.assertWarns(DeprecationWarning, self.gen.randrange, Fraction(3, 1))
    self.assertWarns(DeprecationWarning, raises, '3')
    self.assertWarns(DeprecationWarning, raises, 0, 2.71828)
    self.assertWarns(DeprecationWarning, self.gen.randrange, 0, 2.0)
    self.assertWarns(DeprecationWarning, self.gen.randrange, 0, Fraction(2, 1))
    self.assertWarns(DeprecationWarning, raises, 0, '2')
    raises(0, 42, 0)
    self.assertWarns(DeprecationWarning, raises, 0, 42, 0.0)
    self.assertWarns(DeprecationWarning, raises, 0, 0, 0.0)
    self.assertWarns(DeprecationWarning, raises, 0, 42, 3.14159)
    self.assertWarns(DeprecationWarning, self.gen.randrange, 0, 42, 3.0)
    self.assertWarns(DeprecationWarning, self.gen.randrange, 0, 42, Fraction(3, 1))
    self.assertWarns(DeprecationWarning, raises, 0, 42, '3')
    self.assertWarns(DeprecationWarning, self.gen.randrange, 0, 42, 1.0)
    self.assertWarns(DeprecationWarning, raises, 0, 0, 1.0)
