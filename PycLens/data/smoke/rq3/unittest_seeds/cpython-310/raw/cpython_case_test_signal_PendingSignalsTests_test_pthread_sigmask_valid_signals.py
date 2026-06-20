# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_pthread_sigmask_valid_signals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = signal.pthread_sigmask(signal.SIG_BLOCK, signal.valid_signals())
    self.addCleanup(signal.pthread_sigmask, signal.SIG_SETMASK, s)
    s = signal.pthread_sigmask(signal.SIG_UNBLOCK, signal.valid_signals())
    self.assertLessEqual(s, signal.valid_signals())
