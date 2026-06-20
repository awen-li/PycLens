# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_lazycache_already_cached

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.clearcache()
    lines = linecache.getlines(NONEXISTENT_FILENAME, globals())
    self.assertEqual(False, linecache.lazycache(NONEXISTENT_FILENAME, globals()))
    self.assertEqual(4, len(linecache.cache[NONEXISTENT_FILENAME]))
