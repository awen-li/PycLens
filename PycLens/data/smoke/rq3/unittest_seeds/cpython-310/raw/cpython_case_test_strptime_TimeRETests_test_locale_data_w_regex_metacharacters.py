# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_locale_data_w_regex_metacharacters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    locale_time = _strptime.LocaleTime()
    locale_time.timezone = (frozenset(('utc', 'gmt', 'Tokyo (standard time)')), frozenset('Tokyo (daylight time)'))
    time_re = _strptime.TimeRE(locale_time)
    self.assertTrue(time_re.compile('%Z').match('Tokyo (standard time)'), 'locale data that contains regex metacharacters is not properly escaped')
