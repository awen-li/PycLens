# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualExactTest_test_exactly_equal_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [0.42, 1.974, 1497.4, 23.0, 179.5, 70.0245, 36.587]:
        self.do_exactly_equal_test(x, 0, 0)
