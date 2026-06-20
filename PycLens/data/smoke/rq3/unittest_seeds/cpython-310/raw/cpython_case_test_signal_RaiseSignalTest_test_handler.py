# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: RaiseSignalTest_test_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    is_ok = False

    def handler(a, b):
        nonlocal is_ok
        is_ok = True
    old_signal = signal.signal(signal.SIGINT, handler)
    self.addCleanup(signal.signal, signal.SIGINT, old_signal)
    signal.raise_signal(signal.SIGINT)
    self.assertTrue(is_ok)
