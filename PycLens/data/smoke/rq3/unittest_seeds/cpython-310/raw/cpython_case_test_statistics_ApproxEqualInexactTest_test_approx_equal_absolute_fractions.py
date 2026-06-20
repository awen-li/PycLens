# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_absolute_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta = Fraction(1, 29)
    numerators = [-84, -15, -2, -1, 0, 1, 5, 17, 23, 34, 71]
    for f in (Fraction(n, 29) for n in numerators):
        self.do_approx_equal_abs_test(f, delta)
        self.do_approx_equal_abs_test(f, float(delta))
