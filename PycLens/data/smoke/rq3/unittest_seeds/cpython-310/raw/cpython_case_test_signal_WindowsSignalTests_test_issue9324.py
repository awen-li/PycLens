# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WindowsSignalTests_test_issue9324

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = lambda x, y: None
    checked = set()
    for sig in (signal.SIGABRT, signal.SIGBREAK, signal.SIGFPE, signal.SIGILL, signal.SIGINT, signal.SIGSEGV, signal.SIGTERM):
        if signal.getsignal(sig) is not None:
            signal.signal(sig, signal.signal(sig, handler))
            checked.add(sig)
    self.assertTrue(checked)
    with self.assertRaises(ValueError):
        signal.signal(-1, handler)
    with self.assertRaises(ValueError):
        signal.signal(7, handler)
