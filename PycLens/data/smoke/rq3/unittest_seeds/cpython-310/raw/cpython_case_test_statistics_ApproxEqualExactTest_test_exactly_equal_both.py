# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_both

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [41017, 16.742, -813.02, Fraction(3, 8)]:
        self.do_exactly_equal_test(x, 0.1, 0.01)
    D = Decimal
    self.do_exactly_equal_test(D('7.2'), D('0.1'), D('0.01'))
