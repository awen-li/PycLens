# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CacheTests_test_TimeRE_recreation_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    locale_info = locale.getlocale(locale.LC_TIME)
    try:
        locale.setlocale(locale.LC_TIME, ('en_US', 'UTF8'))
    except locale.Error:
        self.skipTest('test needs en_US.UTF8 locale')
    try:
        _strptime._strptime_time('10', '%d')
        first_time_re = _strptime._TimeRE_cache
        try:
            locale.setlocale(locale.LC_TIME, ('de_DE', 'UTF8'))
            _strptime._strptime_time('10', '%d')
            second_time_re = _strptime._TimeRE_cache
            self.assertIsNot(first_time_re, second_time_re)
        except locale.Error:
            self.skipTest('test needs de_DE.UTF8 locale')
    finally:
        locale.setlocale(locale.LC_TIME, locale_info)
