# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_absolute_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.do_exactly_equal_test(Decimal('3.571'), Decimal('0.01'), 0)
    self.do_exactly_equal_test(-Decimal('81.3971'), Decimal('0.01'), 0)
