# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_long_pattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern = 'Very %spattern' % ('long ' * 1000)
    r = repr(re.compile(pattern))
    self.assertLess(len(r), 300)
    self.assertEqual(r[:30], "re.compile('Very long long lon")
    r = repr(re.compile(pattern, re.I))
    self.assertLess(len(r), 300)
    self.assertEqual(r[:30], "re.compile('Very long long lon")
    self.assertEqual(r[-16:], ', re.IGNORECASE)')
