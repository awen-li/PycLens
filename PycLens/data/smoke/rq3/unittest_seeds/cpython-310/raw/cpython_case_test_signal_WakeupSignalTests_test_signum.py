# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupSignalTests_test_signum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wakeup('def test():\n            signal.signal(signal.SIGUSR1, handler)\n            signal.raise_signal(signal.SIGUSR1)\n            signal.raise_signal(signal.SIGALRM)\n        ', signal.SIGUSR1, signal.SIGALRM)
