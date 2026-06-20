# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_bad_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tz_name = time.tzname[0]
    if tz_name.upper() in ('UTC', 'GMT'):
        self.skipTest('need non-UTC/GMT timezone')
    with support.swap_attr(time, 'tzname', (tz_name, tz_name)), support.swap_attr(time, 'daylight', 1), support.swap_attr(time, 'tzset', lambda : None):
        time.tzname = (tz_name, tz_name)
        time.daylight = 1
        tz_value = _strptime._strptime_time(tz_name, '%Z')[8]
        self.assertEqual(tz_value, -1, '%s lead to a timezone value of %s instead of -1 when time.daylight set to %s and passing in %s' % (time.tzname, tz_value, time.daylight, tz_name))
