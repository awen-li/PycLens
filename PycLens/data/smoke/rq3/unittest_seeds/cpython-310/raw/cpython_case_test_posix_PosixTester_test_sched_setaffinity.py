# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_sched_setaffinity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mask = posix.sched_getaffinity(0)
    if len(mask) > 1:
        mask.pop()
    posix.sched_setaffinity(0, mask)
    self.assertEqual(posix.sched_getaffinity(0), mask)
    self.assertRaises(OSError, posix.sched_setaffinity, 0, [])
    self.assertRaises(ValueError, posix.sched_setaffinity, 0, [-10])
    self.assertRaises(ValueError, posix.sched_setaffinity, 0, map(int, '0X'))
    self.assertRaises(OverflowError, posix.sched_setaffinity, 0, [1 << 128])
    if not sys.platform.startswith('freebsd'):
        self.assertRaises(OSError, posix.sched_setaffinity, -1, mask)
