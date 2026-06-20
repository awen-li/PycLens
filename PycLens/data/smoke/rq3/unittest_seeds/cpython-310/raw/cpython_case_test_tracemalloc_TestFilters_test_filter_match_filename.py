# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestFilters_test_filter_match_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fnmatch(inclusive, filename, pattern):
        f = tracemalloc.Filter(inclusive, pattern)
        return f._match_frame(filename, 0)
    self.assertTrue(fnmatch(True, 'abc', 'abc'))
    self.assertFalse(fnmatch(True, '12356', 'abc'))
    self.assertFalse(fnmatch(True, '<unknown>', 'abc'))
    self.assertFalse(fnmatch(False, 'abc', 'abc'))
    self.assertTrue(fnmatch(False, '12356', 'abc'))
    self.assertTrue(fnmatch(False, '<unknown>', 'abc'))
