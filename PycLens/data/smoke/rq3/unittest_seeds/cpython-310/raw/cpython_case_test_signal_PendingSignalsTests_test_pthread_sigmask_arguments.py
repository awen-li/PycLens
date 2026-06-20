# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_pthread_sigmask_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, signal.pthread_sigmask)
    self.assertRaises(TypeError, signal.pthread_sigmask, 1)
    self.assertRaises(TypeError, signal.pthread_sigmask, 1, 2, 3)
    self.assertRaises(OSError, signal.pthread_sigmask, 1700, [])
    with self.assertRaises(ValueError):
        signal.pthread_sigmask(signal.SIG_BLOCK, [signal.NSIG])
    with self.assertRaises(ValueError):
        signal.pthread_sigmask(signal.SIG_BLOCK, [0])
    with self.assertRaises(ValueError):
        signal.pthread_sigmask(signal.SIG_BLOCK, [1 << 1000])
