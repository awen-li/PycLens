# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_monotonic_settime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = time.monotonic()
    realtime = time.clock_gettime(time.CLOCK_REALTIME)
    try:
        time.clock_settime(time.CLOCK_REALTIME, realtime - 3600)
    except PermissionError as err:
        self.skipTest(err)
    t2 = time.monotonic()
    time.clock_settime(time.CLOCK_REALTIME, realtime)
    self.assertGreaterEqual(t2, t1)
