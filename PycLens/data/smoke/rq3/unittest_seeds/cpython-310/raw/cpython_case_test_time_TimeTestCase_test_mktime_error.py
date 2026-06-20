# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_mktime_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tt = time.gmtime(self.t)
    tzname = time.strftime('%Z', tt)
    self.assertNotEqual(tzname, 'LMT')
    try:
        time.mktime((-1, 1, 1, 0, 0, 0, -1, -1, -1))
    except OverflowError:
        pass
    self.assertEqual(time.strftime('%Z', tt), tzname)
