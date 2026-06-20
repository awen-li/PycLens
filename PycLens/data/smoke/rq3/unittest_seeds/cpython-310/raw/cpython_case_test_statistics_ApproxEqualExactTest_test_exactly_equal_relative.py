# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_relative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [8347, 101.3, -7910.28, Fraction(5, 21)]:
        self.do_exactly_equal_test(x, 0, 0.01)
    self.do_exactly_equal_test(Decimal('11.68'), 0, Decimal('0.01'))
