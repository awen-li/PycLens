# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    with s as sel:
        sel.register(rd, selectors.EVENT_READ)
        sel.register(wr, selectors.EVENT_WRITE)
    self.assertRaises(RuntimeError, s.get_key, rd)
    self.assertRaises(RuntimeError, s.get_key, wr)
