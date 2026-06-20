# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_strsignal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('Interrupt', signal.strsignal(signal.SIGINT))
    self.assertIn('Terminated', signal.strsignal(signal.SIGTERM))
    self.assertIn('Hangup', signal.strsignal(signal.SIGHUP))
