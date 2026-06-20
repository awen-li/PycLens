# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CacheTests_test_new_localetime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    locale_time_id = _strptime._TimeRE_cache.locale_time
    _strptime._TimeRE_cache.locale_time.lang = 'Ni'
    _strptime._strptime_time('10', '%d')
    self.assertIsNot(locale_time_id, _strptime._TimeRE_cache.locale_time)
