# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_sched_rr_get_interval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        interval = posix.sched_rr_get_interval(0)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
        self.skipTest('only works on SCHED_RR processes')
    self.assertIsInstance(interval, float)
    self.assertGreaterEqual(interval, 0.0)
    self.assertLess(interval, 1.0)
