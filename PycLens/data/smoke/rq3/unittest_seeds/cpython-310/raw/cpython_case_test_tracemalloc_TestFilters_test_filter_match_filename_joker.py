# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestFilters_test_filter_match_filename_joker

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fnmatch(filename, pattern):
        filter = tracemalloc.Filter(True, pattern)
        return filter._match_frame(filename, 0)
    self.assertFalse(fnmatch('abc', ''))
    self.assertFalse(fnmatch('', 'abc'))
    self.assertTrue(fnmatch('', ''))
    self.assertTrue(fnmatch('', '*'))
    self.assertTrue(fnmatch('abc', 'abc'))
    self.assertFalse(fnmatch('abc', 'abcd'))
    self.assertFalse(fnmatch('abc', 'def'))
    self.assertTrue(fnmatch('abc', 'a*'))
    self.assertTrue(fnmatch('abc', 'abc*'))
    self.assertFalse(fnmatch('abc', 'b*'))
    self.assertFalse(fnmatch('abc', 'abcd*'))
    self.assertTrue(fnmatch('abc', 'a*c'))
    self.assertTrue(fnmatch('abcdcx', 'a*cx'))
    self.assertFalse(fnmatch('abb', 'a*c'))
    self.assertFalse(fnmatch('abcdce', 'a*cx'))
    self.assertTrue(fnmatch('abcde', 'a*c*e'))
    self.assertTrue(fnmatch('abcbdefeg', 'a*bd*eg'))
    self.assertFalse(fnmatch('abcdd', 'a*c*e'))
    self.assertFalse(fnmatch('abcbdefef', 'a*bd*eg'))
    self.assertTrue(fnmatch('a.pyc', 'a.py'))
    self.assertTrue(fnmatch('a.py', 'a.pyc'))
    if os.name == 'nt':
        self.assertTrue(fnmatch('aBC', 'ABc'))
        self.assertTrue(fnmatch('aBcDe', 'Ab*dE'))
        self.assertTrue(fnmatch('a.pyc', 'a.PY'))
        self.assertTrue(fnmatch('a.py', 'a.PYC'))
    else:
        self.assertFalse(fnmatch('aBC', 'ABc'))
        self.assertFalse(fnmatch('aBcDe', 'Ab*dE'))
        self.assertFalse(fnmatch('a.pyc', 'a.PY'))
        self.assertFalse(fnmatch('a.py', 'a.PYC'))
    if os.name == 'nt':
        self.assertTrue(fnmatch('a/b', 'a\\b'))
        self.assertTrue(fnmatch('a\\b', 'a/b'))
        self.assertTrue(fnmatch('a/b\\c', 'a\\b/c'))
        self.assertTrue(fnmatch('a/b/c', 'a\\b\\c'))
    else:
        self.assertFalse(fnmatch('a/b', 'a\\b'))
        self.assertFalse(fnmatch('a\\b', 'a/b'))
        self.assertFalse(fnmatch('a/b\\c', 'a\\b/c'))
        self.assertFalse(fnmatch('a/b/c', 'a\\b\\c'))
    self.assertFalse(fnmatch('a.pyo', 'a.py'))
