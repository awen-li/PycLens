# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CacheTests_test_time_re_recreation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _strptime._strptime_time('10', '%d')
    _strptime._strptime_time('2005', '%Y')
    _strptime._TimeRE_cache.locale_time.lang = 'Ni'
    original_time_re = _strptime._TimeRE_cache
    _strptime._strptime_time('10', '%d')
    self.assertIsNot(original_time_re, _strptime._TimeRE_cache)
    self.assertEqual(len(_strptime._regex_cache), 1)
