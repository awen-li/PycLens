# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_clearcache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cached = []
    for entry in MODULES:
        filename = os.path.join(MODULE_PATH, entry) + '.py'
        cached.append(filename)
        linecache.getline(filename, 1)
    self.assertNotEqual(cached, [])
    cached_empty = [fn for fn in cached if fn not in linecache.cache]
    self.assertEqual(cached_empty, [])
    linecache.clearcache()
    cached_empty = [fn for fn in cached if fn in linecache.cache]
    self.assertEqual(cached_empty, [])
