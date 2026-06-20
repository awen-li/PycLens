# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheInvalidationTests_test_checkcache_for_deleted_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.checkcache(self.deleted_file)
    self.assertNotIn(self.deleted_file, linecache.cache)
    self.assertIn(self.modified_file, linecache.cache)
    self.assertIn(self.unchanged_file, linecache.cache)
