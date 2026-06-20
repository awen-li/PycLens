# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_fullmatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.fullmatch('a', 'a').span(), (0, 1))
    for string in ('ab', S('ab')):
        self.assertEqual(re.fullmatch('a|ab', string).span(), (0, 2))
    for string in (b'ab', B(b'ab'), bytearray(b'ab'), memoryview(b'ab')):
        self.assertEqual(re.fullmatch(b'a|ab', string).span(), (0, 2))
    for (a, b) in ('àß', 'аб', '𝒜𝒞'):
        r = '%s|%s' % (a, a + b)
        self.assertEqual(re.fullmatch(r, a + b).span(), (0, 2))
    self.assertEqual(re.fullmatch('.*?$', 'abc').span(), (0, 3))
    self.assertEqual(re.fullmatch('.*?', 'abc').span(), (0, 3))
    self.assertEqual(re.fullmatch('a.*?b', 'ab').span(), (0, 2))
    self.assertEqual(re.fullmatch('a.*?b', 'abb').span(), (0, 3))
    self.assertEqual(re.fullmatch('a.*?b', 'axxb').span(), (0, 4))
    self.assertIsNone(re.fullmatch('a+', 'ab'))
    self.assertIsNone(re.fullmatch('abc$', 'abc\n'))
    self.assertIsNone(re.fullmatch('abc\\Z', 'abc\n'))
    self.assertIsNone(re.fullmatch('(?m)abc$', 'abc\n'))
    self.assertEqual(re.fullmatch('ab(?=c)cd', 'abcd').span(), (0, 4))
    self.assertEqual(re.fullmatch('ab(?<=b)cd', 'abcd').span(), (0, 4))
    self.assertEqual(re.fullmatch('(?=a|ab)ab', 'ab').span(), (0, 2))
    self.assertEqual(re.compile('bc').fullmatch('abcd', pos=1, endpos=3).span(), (1, 3))
    self.assertEqual(re.compile('.*?$').fullmatch('abcd', pos=1, endpos=3).span(), (1, 3))
    self.assertEqual(re.compile('.*?').fullmatch('abcd', pos=1, endpos=3).span(), (1, 3))
