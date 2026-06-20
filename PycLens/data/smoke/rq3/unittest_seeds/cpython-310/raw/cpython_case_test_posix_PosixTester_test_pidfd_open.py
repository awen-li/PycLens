# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pidfd_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(OSError) as cm:
        os.pidfd_open(-1)
    if cm.exception.errno == errno.ENOSYS:
        self.skipTest('system does not support pidfd_open')
    if isinstance(cm.exception, PermissionError):
        self.skipTest(f'pidfd_open syscall blocked: {cm.exception!r}')
    self.assertEqual(cm.exception.errno, errno.EINVAL)
    os.close(os.pidfd_open(os.getpid(), 0))
