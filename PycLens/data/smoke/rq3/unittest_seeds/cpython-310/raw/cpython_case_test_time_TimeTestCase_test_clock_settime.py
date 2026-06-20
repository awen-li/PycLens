# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_clock_settime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.clock_gettime(time.CLOCK_REALTIME)
    try:
        time.clock_settime(time.CLOCK_REALTIME, t)
    except PermissionError:
        pass
    if hasattr(time, 'CLOCK_MONOTONIC'):
        self.assertRaises(OSError, time.clock_settime, time.CLOCK_MONOTONIC, 0)
