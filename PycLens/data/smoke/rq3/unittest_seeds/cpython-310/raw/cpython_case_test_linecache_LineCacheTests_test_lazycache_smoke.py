# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_lazycache_smoke

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = linecache.getlines(NONEXISTENT_FILENAME, globals())
    linecache.clearcache()
    self.assertEqual(True, linecache.lazycache(NONEXISTENT_FILENAME, globals()))
    self.assertEqual(1, len(linecache.cache[NONEXISTENT_FILENAME]))
    self.assertEqual(lines, linecache.getlines(NONEXISTENT_FILENAME))
