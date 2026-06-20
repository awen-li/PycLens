# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_unregister

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    s.register(rd, selectors.EVENT_READ)
    s.unregister(rd)
    self.assertRaises(KeyError, s.unregister, 999999)
    self.assertRaises(KeyError, s.unregister, rd)
