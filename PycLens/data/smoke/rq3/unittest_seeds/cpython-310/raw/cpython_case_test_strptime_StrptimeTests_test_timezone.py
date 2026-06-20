# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    strp_output = _strptime._strptime_time('UTC', '%Z')
    self.assertEqual(strp_output.tm_isdst, 0)
    strp_output = _strptime._strptime_time('GMT', '%Z')
    self.assertEqual(strp_output.tm_isdst, 0)
    time_tuple = time.localtime()
    strf_output = time.strftime('%Z')
    strp_output = _strptime._strptime_time(strf_output, '%Z')
    locale_time = _strptime.LocaleTime()
    if time.tzname[0] != time.tzname[1] or not time.daylight:
        self.assertTrue(strp_output[8] == time_tuple[8], "timezone check failed; '%s' -> %s != %s" % (strf_output, strp_output[8], time_tuple[8]))
    else:
        self.assertTrue(strp_output[8] == -1, 'LocaleTime().timezone has duplicate values and time.daylight but timezone value not set to -1')
