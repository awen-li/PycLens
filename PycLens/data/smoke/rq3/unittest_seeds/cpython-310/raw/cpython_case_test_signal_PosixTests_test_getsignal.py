# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: PosixTests_test_getsignal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hup = signal.signal(signal.SIGHUP, self.trivial_signal_handler)
    self.assertIsInstance(hup, signal.Handlers)
    self.assertEqual(signal.getsignal(signal.SIGHUP), self.trivial_signal_handler)
    signal.signal(signal.SIGHUP, hup)
    self.assertEqual(signal.getsignal(signal.SIGHUP), hup)
