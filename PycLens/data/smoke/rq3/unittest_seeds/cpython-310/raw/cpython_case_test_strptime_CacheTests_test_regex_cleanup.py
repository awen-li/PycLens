# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CacheTests_test_regex_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        del _strptime._regex_cache['%d']
    except KeyError:
        pass
    bogus_key = 0
    while len(_strptime._regex_cache) <= _strptime._CACHE_MAX_SIZE:
        _strptime._regex_cache[bogus_key] = None
        bogus_key += 1
    _strptime._strptime_time('10', '%d')
    self.assertEqual(len(_strptime._regex_cache), 1)
