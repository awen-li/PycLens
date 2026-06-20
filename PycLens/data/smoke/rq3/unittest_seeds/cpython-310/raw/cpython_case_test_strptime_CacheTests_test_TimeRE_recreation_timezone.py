# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CacheTests_test_TimeRE_recreation_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldtzname = time.tzname
    tm = _strptime._strptime_time(time.tzname[0], '%Z')
    self.assertEqual(tm.tm_isdst, 0)
    tm = _strptime._strptime_time(time.tzname[1], '%Z')
    self.assertEqual(tm.tm_isdst, 1)
    first_time_re = _strptime._TimeRE_cache
    os.environ['TZ'] = 'EST+05EDT,M3.2.0,M11.1.0'
    time.tzset()
    tm = _strptime._strptime_time(time.tzname[0], '%Z')
    self.assertEqual(tm.tm_isdst, 0)
    tm = _strptime._strptime_time(time.tzname[1], '%Z')
    self.assertEqual(tm.tm_isdst, 1)
    second_time_re = _strptime._TimeRE_cache
    self.assertIsNot(first_time_re, second_time_re)
    with self.assertRaises(ValueError):
        _strptime._strptime_time(oldtzname[0], '%Z')
    with self.assertRaises(ValueError):
        _strptime._strptime_time(oldtzname[1], '%Z')
