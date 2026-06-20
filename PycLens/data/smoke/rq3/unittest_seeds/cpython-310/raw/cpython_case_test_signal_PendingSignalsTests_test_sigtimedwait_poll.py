# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigtimedwait_poll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.wait_helper(signal.SIGALRM, "\n        def test(signum):\n            import os\n            os.kill(os.getpid(), signum)\n            info = signal.sigtimedwait([signum], 0)\n            if info.si_signo != signum:\n                raise Exception('info.si_signo != %s' % signum)\n        ")
