# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_valid_signals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = signal.valid_signals()
    self.assertIsInstance(s, set)
    self.assertIn(signal.Signals.SIGINT, s)
    self.assertIn(signal.Signals.SIGALRM, s)
    self.assertNotIn(0, s)
    self.assertNotIn(signal.NSIG, s)
    self.assertLess(len(s), signal.NSIG)
