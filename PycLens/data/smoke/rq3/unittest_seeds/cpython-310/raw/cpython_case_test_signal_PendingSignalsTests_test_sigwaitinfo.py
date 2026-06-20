# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigwaitinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.wait_helper(signal.SIGALRM, '\n        def test(signum):\n            signal.alarm(1)\n            info = signal.sigwaitinfo([signum])\n            if info.si_signo != signum:\n                raise Exception("info.si_signo != %s" % signum)\n        ')
