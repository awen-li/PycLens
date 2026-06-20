# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    s.register(wr, selectors.EVENT_WRITE)
    t = time()
    self.assertEqual(1, len(s.select(0)))
    self.assertEqual(1, len(s.select(-1)))
    self.assertLess(time() - t, 0.5)
    s.unregister(wr)
    s.register(rd, selectors.EVENT_READ)
    t = time()
    self.assertFalse(s.select(0))
    self.assertFalse(s.select(-1))
    self.assertLess(time() - t, 0.5)
    t0 = time()
    self.assertFalse(s.select(1))
    t1 = time()
    dt = t1 - t0
    self.assertTrue(0.8 <= dt <= 2.0, dt)
