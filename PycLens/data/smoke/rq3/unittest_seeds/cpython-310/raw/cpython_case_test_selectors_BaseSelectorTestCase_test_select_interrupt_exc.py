# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_select_interrupt_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()

    class InterruptSelect(Exception):
        pass

    def handler(*args):
        raise InterruptSelect
    orig_alrm_handler = signal.signal(signal.SIGALRM, handler)
    self.addCleanup(signal.signal, signal.SIGALRM, orig_alrm_handler)
    try:
        signal.alarm(1)
        s.register(rd, selectors.EVENT_READ)
        t = time()
        with self.assertRaises(InterruptSelect):
            s.select(30)
        self.assertLess(time() - t, 5.0)
    finally:
        signal.alarm(0)
