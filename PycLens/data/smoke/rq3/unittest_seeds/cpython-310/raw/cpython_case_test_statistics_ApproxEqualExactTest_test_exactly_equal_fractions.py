# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    F = Fraction
    for f in [F(1, 2), F(0), F(5, 3), F(9, 7), F(35, 36), F(3, 7)]:
        self.do_exactly_equal_test(f, 0, 0)
