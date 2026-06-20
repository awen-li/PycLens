# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualUnequalTest_test_exactly_unequal_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    F = Fraction
    for f in [F(1, 5), F(7, 9), F(12, 11), F(101, 99023)]:
        self.do_exactly_unequal_test(f)
