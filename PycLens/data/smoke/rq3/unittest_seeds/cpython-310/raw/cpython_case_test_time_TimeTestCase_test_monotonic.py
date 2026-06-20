# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_monotonic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    times = [time.monotonic() for n in range(100)]
    t1 = times[0]
    for t2 in times[1:]:
        self.assertGreaterEqual(t2, t1, 'times=%s' % times)
        t1 = t2
    t1 = time.monotonic()
    time.sleep(0.5)
    t2 = time.monotonic()
    dt = t2 - t1
    self.assertGreater(t2, t1)
    self.assertTrue(0.45 <= dt)
    info = time.get_clock_info('monotonic')
    self.assertTrue(info.monotonic)
    self.assertFalse(info.adjustable)
