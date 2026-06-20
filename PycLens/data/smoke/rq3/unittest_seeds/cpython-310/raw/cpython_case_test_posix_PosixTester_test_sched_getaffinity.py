# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_sched_getaffinity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mask = posix.sched_getaffinity(0)
    self.assertIsInstance(mask, set)
    self.assertGreaterEqual(len(mask), 1)
    if not sys.platform.startswith('freebsd'):
        self.assertRaises(OSError, posix.sched_getaffinity, -1)
    for cpu in mask:
        self.assertIsInstance(cpu, int)
        self.assertGreaterEqual(cpu, 0)
        self.assertLess(cpu, 1 << 32)
