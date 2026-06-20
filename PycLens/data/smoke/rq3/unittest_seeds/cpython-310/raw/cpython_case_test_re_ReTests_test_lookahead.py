# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_lookahead

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('(a(?=\\s[^a]))', 'a b').group(1), 'a')
    self.assertEqual(re.match('(a(?=\\s[^a]*))', 'a b').group(1), 'a')
    self.assertEqual(re.match('(a(?=\\s[abc]))', 'a b').group(1), 'a')
    self.assertEqual(re.match('(a(?=\\s[abc]*))', 'a bc').group(1), 'a')
    self.assertEqual(re.match('(a)(?=\\s\\1)', 'a a').group(1), 'a')
    self.assertEqual(re.match('(a)(?=\\s\\1*)', 'a aa').group(1), 'a')
    self.assertEqual(re.match('(a)(?=\\s(abc|a))', 'a a').group(1), 'a')
    self.assertEqual(re.match('(a(?!\\s[^a]))', 'a a').group(1), 'a')
    self.assertEqual(re.match('(a(?!\\s[abc]))', 'a d').group(1), 'a')
    self.assertEqual(re.match('(a)(?!\\s\\1)', 'a b').group(1), 'a')
    self.assertEqual(re.match('(a)(?!\\s(abc|a))', 'a b').group(1), 'a')
    self.assertTrue(re.match('(a)b(?=\\1)a', 'aba'))
    self.assertIsNone(re.match('(a)b(?=\\1)c', 'abac'))
    self.assertTrue(re.match('(?:(a)|(x))b(?=(?(2)x|c))c', 'abc'))
    self.assertIsNone(re.match('(?:(a)|(x))b(?=(?(2)c|x))c', 'abc'))
    self.assertTrue(re.match('(?:(a)|(x))b(?=(?(2)x|c))c', 'abc'))
    self.assertIsNone(re.match('(?:(a)|(x))b(?=(?(1)b|x))c', 'abc'))
    self.assertTrue(re.match('(?:(a)|(x))b(?=(?(1)c|x))c', 'abc'))
    self.assertTrue(re.match('(a)b(?=(?(2)x|c))(c)', 'abc'))
    self.assertIsNone(re.match('(a)b(?=(?(2)b|x))(c)', 'abc'))
    self.assertTrue(re.match('(a)b(?=(?(1)c|x))(c)', 'abc'))
