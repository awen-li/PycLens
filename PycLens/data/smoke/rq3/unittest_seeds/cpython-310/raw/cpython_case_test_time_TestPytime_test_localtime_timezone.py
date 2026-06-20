# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestPytime_test_localtime_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lt = time.localtime()
    self.assertTrue(hasattr(lt, 'tm_gmtoff'))
    self.assertTrue(hasattr(lt, 'tm_zone'))
    if lt.tm_gmtoff is None:
        self.assertTrue(not hasattr(time, 'timezone'))
    else:
        self.assertEqual(lt.tm_gmtoff, -[time.timezone, time.altzone][lt.tm_isdst])
    if lt.tm_zone is None:
        self.assertTrue(not hasattr(time, 'tzname'))
    else:
        self.assertEqual(lt.tm_zone, time.tzname[lt.tm_isdst])
    t = time.mktime(lt)
    t9 = time.mktime(lt[:9])
    self.assertEqual(t, t9)
    new_lt = time.localtime(t)
    new_lt9 = time.localtime(t9)
    self.assertEqual(new_lt, lt)
    self.assertEqual(new_lt.tm_gmtoff, lt.tm_gmtoff)
    self.assertEqual(new_lt.tm_zone, lt.tm_zone)
    self.assertEqual(new_lt9, lt)
    self.assertEqual(new_lt.tm_gmtoff, lt.tm_gmtoff)
    self.assertEqual(new_lt9.tm_zone, lt.tm_zone)
