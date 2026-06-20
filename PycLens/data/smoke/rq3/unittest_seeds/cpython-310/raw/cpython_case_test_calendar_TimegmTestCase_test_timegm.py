# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: TimegmTestCase_test_timegm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for secs in self.TIMESTAMPS:
        tuple = time.gmtime(secs)
        self.assertEqual(secs, calendar.timegm(tuple))
