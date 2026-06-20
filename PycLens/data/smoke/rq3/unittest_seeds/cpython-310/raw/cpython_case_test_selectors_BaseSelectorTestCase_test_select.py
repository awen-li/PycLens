# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_select

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    s.register(rd, selectors.EVENT_READ)
    wr_key = s.register(wr, selectors.EVENT_WRITE)
    result = s.select()
    for (key, events) in result:
        self.assertTrue(isinstance(key, selectors.SelectorKey))
        self.assertTrue(events)
        self.assertFalse(events & ~(selectors.EVENT_READ | selectors.EVENT_WRITE))
    self.assertEqual([(wr_key, selectors.EVENT_WRITE)], result)
