# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestFindLongest_test_longest_match_with_popular_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 'dabcd'
    b = 'd' * 100 + 'abc' + 'd' * 100
    sm = difflib.SequenceMatcher(a=a, b=b)
    match = sm.find_longest_match(0, len(a), 0, len(b))
    self.assertEqual(match.a, 0)
    self.assertEqual(match.b, 99)
    self.assertEqual(match.size, 5)
    self.assertEqual(a[match.a:match.a + match.size], b[match.b:match.b + match.size])
    self.assertFalse(self.longer_match_exists(a, b, match.size))
