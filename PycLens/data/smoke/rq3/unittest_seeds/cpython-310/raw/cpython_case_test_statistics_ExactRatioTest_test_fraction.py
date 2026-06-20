# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_fraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    numerators = (-5, 1, 12, 38)
    for n in numerators:
        f = Fraction(n, 37)
        self.assertEqual(statistics._exact_ratio(f), (n, 37))
