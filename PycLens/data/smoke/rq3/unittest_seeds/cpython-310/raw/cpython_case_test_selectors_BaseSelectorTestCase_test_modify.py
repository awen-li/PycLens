# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_modify

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    key = s.register(rd, selectors.EVENT_READ)
    key2 = s.modify(rd, selectors.EVENT_WRITE)
    self.assertNotEqual(key.events, key2.events)
    self.assertEqual(key2, s.get_key(rd))
    s.unregister(rd)
    d1 = object()
    d2 = object()
    key = s.register(rd, selectors.EVENT_READ, d1)
    key2 = s.modify(rd, selectors.EVENT_READ, d2)
    self.assertEqual(key.events, key2.events)
    self.assertNotEqual(key.data, key2.data)
    self.assertEqual(key2, s.get_key(rd))
    self.assertEqual(key2.data, d2)
    self.assertRaises(KeyError, s.modify, 999999, selectors.EVENT_READ)
    d3 = object()
    s.register = unittest.mock.Mock()
    s.unregister = unittest.mock.Mock()
    s.modify(rd, selectors.EVENT_READ, d3)
    self.assertFalse(s.register.called)
    self.assertFalse(s.unregister.called)
