# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_dollar_matches_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern = re.compile('$')
    self.assertEqual(pattern.sub('#', 'a\nb\n'), 'a\nb#\n#')
    self.assertEqual(pattern.sub('#', 'a\nb\nc'), 'a\nb\nc#')
    self.assertEqual(pattern.sub('#', '\n'), '#\n#')
    pattern = re.compile('$', re.MULTILINE)
    self.assertEqual(pattern.sub('#', 'a\nb\n'), 'a#\nb#\n#')
    self.assertEqual(pattern.sub('#', 'a\nb\nc'), 'a#\nb#\nc#')
    self.assertEqual(pattern.sub('#', '\n'), '#\n#')
