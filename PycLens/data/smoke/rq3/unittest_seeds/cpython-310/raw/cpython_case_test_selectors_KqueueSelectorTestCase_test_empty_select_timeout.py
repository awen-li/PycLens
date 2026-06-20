# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: KqueueSelectorTestCase_test_empty_select_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    t0 = time()
    self.assertEqual(s.select(1), [])
    t1 = time()
    dt = t1 - t0
    self.assertTrue(0.8 <= dt <= 2.0, dt)
