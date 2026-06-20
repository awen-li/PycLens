# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    key = s.register(rd, selectors.EVENT_READ, 'data')
    self.assertIsInstance(key, selectors.SelectorKey)
    self.assertEqual(key.fileobj, rd)
    self.assertEqual(key.fd, rd.fileno())
    self.assertEqual(key.events, selectors.EVENT_READ)
    self.assertEqual(key.data, 'data')
    self.assertRaises(ValueError, s.register, 0, 999999)
    self.assertRaises(ValueError, s.register, -10, selectors.EVENT_READ)
    self.assertRaises(KeyError, s.register, rd, selectors.EVENT_READ)
    self.assertRaises(KeyError, s.register, rd.fileno(), selectors.EVENT_READ)
