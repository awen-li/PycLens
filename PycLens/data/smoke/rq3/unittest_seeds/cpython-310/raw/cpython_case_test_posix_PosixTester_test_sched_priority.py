# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_sched_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = posix.SCHED_RR
    lo = posix.sched_get_priority_min(pol)
    hi = posix.sched_get_priority_max(pol)
    self.assertIsInstance(lo, int)
    self.assertIsInstance(hi, int)
    self.assertGreaterEqual(hi, lo)
    if sys.platform != 'darwin':
        self.assertRaises(OSError, posix.sched_get_priority_min, -23)
        self.assertRaises(OSError, posix.sched_get_priority_max, -23)
