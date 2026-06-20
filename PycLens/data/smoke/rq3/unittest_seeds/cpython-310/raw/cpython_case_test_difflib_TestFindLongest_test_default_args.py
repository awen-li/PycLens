# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestFindLongest_test_default_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 'foo bar'
    b = 'foo baz bar'
    sm = difflib.SequenceMatcher(a=a, b=b)
    match = sm.find_longest_match()
    self.assertEqual(match.a, 0)
    self.assertEqual(match.b, 0)
    self.assertEqual(match.size, 6)
    self.assertEqual(a[match.a:match.a + match.size], b[match.b:match.b + match.size])
    self.assertFalse(self.longer_match_exists(a, b, match.size))
    match = sm.find_longest_match(alo=2, blo=4)
    self.assertEqual(match.a, 3)
    self.assertEqual(match.b, 7)
    self.assertEqual(match.size, 4)
    self.assertEqual(a[match.a:match.a + match.size], b[match.b:match.b + match.size])
    self.assertFalse(self.longer_match_exists(a[2:], b[4:], match.size))
    match = sm.find_longest_match(bhi=5, blo=1)
    self.assertEqual(match.a, 1)
    self.assertEqual(match.b, 1)
    self.assertEqual(match.size, 4)
    self.assertEqual(a[match.a:match.a + match.size], b[match.b:match.b + match.size])
    self.assertFalse(self.longer_match_exists(a, b[1:5], match.size))
