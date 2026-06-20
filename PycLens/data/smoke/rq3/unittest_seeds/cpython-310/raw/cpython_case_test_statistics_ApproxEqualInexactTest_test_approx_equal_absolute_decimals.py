# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_absolute_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta = Decimal('0.01')
    for d in map(Decimal, '1.0 3.5 36.08 61.79 7912.3648'.split()):
        self.do_approx_equal_abs_test(d, delta)
        self.do_approx_equal_abs_test(-d, delta)
