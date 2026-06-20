# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_lookbehind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.match('ab(?<=b)c', 'abc'))
    self.assertIsNone(re.match('ab(?<=c)c', 'abc'))
    self.assertIsNone(re.match('ab(?<!b)c', 'abc'))
    self.assertTrue(re.match('ab(?<!c)c', 'abc'))
    self.assertTrue(re.match('(a)a(?<=\\1)c', 'aac'))
    self.assertIsNone(re.match('(a)b(?<=\\1)a', 'abaa'))
    self.assertIsNone(re.match('(a)a(?<!\\1)c', 'aac'))
    self.assertTrue(re.match('(a)b(?<!\\1)a', 'abaa'))
    self.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(2)x|c))c', 'abc'))
    self.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(2)b|x))c', 'abc'))
    self.assertTrue(re.match('(?:(a)|(x))b(?<=(?(2)x|b))c', 'abc'))
    self.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(1)c|x))c', 'abc'))
    self.assertTrue(re.match('(?:(a)|(x))b(?<=(?(1)b|x))c', 'abc'))
    self.assertRaises(re.error, re.compile, '(a)b(?<=(?(2)b|x))(c)')
    self.assertIsNone(re.match('(a)b(?<=(?(1)c|x))(c)', 'abc'))
    self.assertTrue(re.match('(a)b(?<=(?(1)b|x))(c)', 'abc'))
    self.assertRaises(re.error, re.compile, '(a)b(?<=(.)\\2)(c)')
    self.assertRaises(re.error, re.compile, '(a)b(?<=(?P<a>.)(?P=a))(c)')
    self.assertRaises(re.error, re.compile, '(a)b(?<=(a)(?(2)b|x))(c)')
    self.assertRaises(re.error, re.compile, '(a)b(?<=(.)(?<=\\2))(c)')
