# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_select_interrupt_noraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    orig_alrm_handler = signal.signal(signal.SIGALRM, lambda *args: None)
    self.addCleanup(signal.signal, signal.SIGALRM, orig_alrm_handler)
    try:
        signal.alarm(1)
        s.register(rd, selectors.EVENT_READ)
        t = time()
        self.assertFalse(s.select(1.5))
        self.assertGreaterEqual(time() - t, 1.0)
    finally:
        signal.alarm(0)
