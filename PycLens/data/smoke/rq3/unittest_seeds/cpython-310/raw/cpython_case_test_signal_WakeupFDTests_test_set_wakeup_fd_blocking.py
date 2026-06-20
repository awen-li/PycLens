# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupFDTests_test_set_wakeup_fd_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rfd, wfd) = os.pipe()
    self.addCleanup(os.close, rfd)
    self.addCleanup(os.close, wfd)
    os.set_blocking(wfd, True)
    with self.assertRaises(ValueError) as cm:
        signal.set_wakeup_fd(wfd)
    self.assertEqual(str(cm.exception), 'the fd %s must be in non-blocking mode' % wfd)
    os.set_blocking(wfd, False)
    signal.set_wakeup_fd(wfd)
    signal.set_wakeup_fd(-1)
