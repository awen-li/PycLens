# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from fractions import Fraction
    fraction_examples = [(Fraction(1, 100000000) + 1, Fraction(1)), (Fraction(100000001), Fraction(100000000)), (Fraction(10 ** 8 + 1, 10 ** 28), Fraction(1, 10 ** 20))]
    self.assertAllClose(fraction_examples, rel_tol=1e-08)
    self.assertAllNotClose(fraction_examples, rel_tol=1e-09)
