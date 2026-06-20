# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: GenericTests_test_enums

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in dir(signal):
        sig = getattr(signal, name)
        if name in {'SIG_DFL', 'SIG_IGN'}:
            self.assertIsInstance(sig, signal.Handlers)
        elif name in {'SIG_BLOCK', 'SIG_UNBLOCK', 'SIG_SETMASK'}:
            self.assertIsInstance(sig, signal.Sigmasks)
        elif name.startswith('SIG') and (not name.startswith('SIG_')):
            self.assertIsInstance(sig, signal.Signals)
        elif name.startswith('CTRL_'):
            self.assertIsInstance(sig, signal.Signals)
            self.assertEqual(sys.platform, 'win32')
