# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    for d in map(D, '8.2 31.274 912.04 16.745 1.2047'.split()):
        self.do_exactly_equal_test(d, 0, 0)
