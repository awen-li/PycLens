# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigtimedwait_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.wait_helper(signal.SIGALRM, '\n        def test(signum):\n            received = signal.sigtimedwait([signum], 1.0)\n            if received is not None:\n                raise Exception("received=%r" % (received,))\n        ')
