# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_groupref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('^(\\|)?([^()]+)\\1$', '|a|').groups(), ('|', 'a'))
    self.assertEqual(re.match('^(\\|)?([^()]+)\\1?$', 'a').groups(), (None, 'a'))
    self.assertIsNone(re.match('^(\\|)?([^()]+)\\1$', 'a|'))
    self.assertIsNone(re.match('^(\\|)?([^()]+)\\1$', '|a'))
    self.assertEqual(re.match('^(?:(a)|c)(\\1)$', 'aa').groups(), ('a', 'a'))
    self.assertEqual(re.match('^(?:(a)|c)(\\1)?$', 'c').groups(), (None, None))
    self.checkPatternError('(abc\\1)', 'cannot refer to an open group', 4)
