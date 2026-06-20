# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_unregister_after_fd_close_and_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    (r, w) = (rd.fileno(), wr.fileno())
    s.register(r, selectors.EVENT_READ)
    s.register(w, selectors.EVENT_WRITE)
    (rd2, wr2) = self.make_socketpair()
    rd.close()
    wr.close()
    os.dup2(rd2.fileno(), r)
    os.dup2(wr2.fileno(), w)
    self.addCleanup(os.close, r)
    self.addCleanup(os.close, w)
    s.unregister(r)
    s.unregister(w)
