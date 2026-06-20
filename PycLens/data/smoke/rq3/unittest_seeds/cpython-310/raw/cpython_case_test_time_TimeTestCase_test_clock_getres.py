# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_clock_getres

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = time.clock_getres(time.CLOCK_REALTIME)
    self.assertGreater(res, 0.0)
    self.assertLessEqual(res, 1.0)
