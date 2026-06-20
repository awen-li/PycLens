# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_absolute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in [16, 1013, 1372, 1198, 971, 4]:
        self.do_exactly_equal_test(n, 0.01, 0)
        self.do_exactly_equal_test(n / 10, 0.01, 0)
        f = Fraction(n, 1234)
        self.do_exactly_equal_test(f, 0.01, 0)
