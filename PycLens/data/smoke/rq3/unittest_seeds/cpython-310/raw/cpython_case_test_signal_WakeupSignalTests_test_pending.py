# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupSignalTests_test_pending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wakeup('def test():\n            signum1 = signal.SIGUSR1\n            signum2 = signal.SIGUSR2\n\n            signal.signal(signum1, handler)\n            signal.signal(signum2, handler)\n\n            signal.pthread_sigmask(signal.SIG_BLOCK, (signum1, signum2))\n            signal.raise_signal(signum1)\n            signal.raise_signal(signum2)\n            # Unblocking the 2 signals calls the C signal handler twice\n            signal.pthread_sigmask(signal.SIG_UNBLOCK, (signum1, signum2))\n        ', signal.SIGUSR1, signal.SIGUSR2, ordered=False)
