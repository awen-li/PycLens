# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PidfdSignalTest_test_pidfd_send_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(OSError) as cm:
        signal.pidfd_send_signal(0, signal.SIGINT)
    if cm.exception.errno == errno.ENOSYS:
        self.skipTest('kernel does not support pidfds')
    elif cm.exception.errno == errno.EPERM:
        self.skipTest('Not enough privileges to use pidfs')
    self.assertEqual(cm.exception.errno, errno.EBADF)
    my_pidfd = os.open(f'/proc/{os.getpid()}', os.O_DIRECTORY)
    self.addCleanup(os.close, my_pidfd)
    with self.assertRaisesRegex(TypeError, '^siginfo must be None$'):
        signal.pidfd_send_signal(my_pidfd, signal.SIGINT, object(), 0)
    with self.assertRaises(KeyboardInterrupt):
        signal.pidfd_send_signal(my_pidfd, signal.SIGINT)
