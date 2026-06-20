# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_527371

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(re.match('(a)?a', 'a').lastindex)
    self.assertEqual(re.match('(a)(b)?b', 'ab').lastindex, 1)
    self.assertEqual(re.match('(?P<a>a)(?P<b>b)?b', 'ab').lastgroup, 'a')
    self.assertEqual(re.match('(?P<a>a(b))', 'ab').lastgroup, 'a')
    self.assertEqual(re.match('((a))', 'a').lastindex, 1)
