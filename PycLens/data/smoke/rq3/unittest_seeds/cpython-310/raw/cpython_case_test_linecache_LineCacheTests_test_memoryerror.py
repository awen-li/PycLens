# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_memoryerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = linecache.getlines(FILENAME)
    self.assertTrue(lines)

    def raise_memoryerror(*args, **kwargs):
        raise MemoryError
    with support.swap_attr(linecache, 'updatecache', raise_memoryerror):
        lines2 = linecache.getlines(FILENAME)
    self.assertEqual(lines2, lines)
    linecache.clearcache()
    with support.swap_attr(linecache, 'updatecache', raise_memoryerror):
        lines3 = linecache.getlines(FILENAME)
    self.assertEqual(lines3, [])
    self.assertEqual(linecache.getlines(FILENAME), lines)
