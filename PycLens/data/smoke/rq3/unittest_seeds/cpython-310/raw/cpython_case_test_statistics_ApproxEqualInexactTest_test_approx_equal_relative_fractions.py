# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_relative_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    F = Fraction
    delta = Fraction(3, 8)
    for f in [F(3, 84), F(17, 30), F(49, 50), F(92, 85)]:
        for d in (delta, float(delta)):
            self.do_approx_equal_rel_test(f, d)
            self.do_approx_equal_rel_test(-f, d)
