# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    mapping = s.get_map()
    (rd, wr) = self.make_socketpair()
    s.register(rd, selectors.EVENT_READ)
    s.register(wr, selectors.EVENT_WRITE)
    s.close()
    self.assertRaises(RuntimeError, s.get_key, rd)
    self.assertRaises(RuntimeError, s.get_key, wr)
    self.assertRaises(KeyError, mapping.__getitem__, rd)
    self.assertRaises(KeyError, mapping.__getitem__, wr)
