# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_relative_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in map(Decimal, '0.02 1.0 5.7 13.67 94.138 91027.9321'.split()):
        self.do_approx_equal_rel_test(d, Decimal('0.001'))
        self.do_approx_equal_rel_test(-d, Decimal('0.05'))
