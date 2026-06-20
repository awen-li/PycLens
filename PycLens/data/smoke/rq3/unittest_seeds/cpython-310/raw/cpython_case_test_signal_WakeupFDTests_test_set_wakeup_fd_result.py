# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupFDTests_test_set_wakeup_fd_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r1, w1) = os.pipe()
    self.addCleanup(os.close, r1)
    self.addCleanup(os.close, w1)
    (r2, w2) = os.pipe()
    self.addCleanup(os.close, r2)
    self.addCleanup(os.close, w2)
    if hasattr(os, 'set_blocking'):
        os.set_blocking(w1, False)
        os.set_blocking(w2, False)
    signal.set_wakeup_fd(w1)
    self.assertEqual(signal.set_wakeup_fd(w2), w1)
    self.assertEqual(signal.set_wakeup_fd(-1), w2)
    self.assertEqual(signal.set_wakeup_fd(-1), -1)
