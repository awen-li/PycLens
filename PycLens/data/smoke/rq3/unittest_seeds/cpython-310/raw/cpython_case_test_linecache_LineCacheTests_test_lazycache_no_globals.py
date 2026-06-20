# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_lazycache_no_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = linecache.getlines(FILENAME)
    linecache.clearcache()
    self.assertEqual(False, linecache.lazycache(FILENAME, None))
    self.assertEqual(lines, linecache.getlines(FILENAME))
