# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in [42, 19740, 14974, 230, 1795, 700245, 36587]:
        self.do_exactly_equal_test(n, 0, 0)
