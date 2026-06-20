# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_clock_monotonic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = time.clock_gettime(time.CLOCK_MONOTONIC)
    b = time.clock_gettime(time.CLOCK_MONOTONIC)
    self.assertLessEqual(a, b)
