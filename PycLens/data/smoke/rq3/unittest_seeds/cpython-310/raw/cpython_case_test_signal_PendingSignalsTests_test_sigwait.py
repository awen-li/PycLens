# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PendingSignalsTests_test_sigwait

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.wait_helper(signal.SIGALRM, "\n        def test(signum):\n            signal.alarm(1)\n            received = signal.sigwait([signum])\n            assert isinstance(received, signal.Signals), received\n            if received != signum:\n                raise Exception('received %s, not %s' % (received, signum))\n        ")
