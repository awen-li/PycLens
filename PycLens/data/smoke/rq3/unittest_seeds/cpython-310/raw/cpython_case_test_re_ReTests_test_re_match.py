# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for string in ('a', S('a')):
        self.assertEqual(re.match('a', string).groups(), ())
        self.assertEqual(re.match('(a)', string).groups(), ('a',))
        self.assertEqual(re.match('(a)', string).group(0), 'a')
        self.assertEqual(re.match('(a)', string).group(1), 'a')
        self.assertEqual(re.match('(a)', string).group(1, 1), ('a', 'a'))
    for string in (b'a', B(b'a'), bytearray(b'a'), memoryview(b'a')):
        self.assertEqual(re.match(b'a', string).groups(), ())
        self.assertEqual(re.match(b'(a)', string).groups(), (b'a',))
        self.assertEqual(re.match(b'(a)', string).group(0), b'a')
        self.assertEqual(re.match(b'(a)', string).group(1), b'a')
        self.assertEqual(re.match(b'(a)', string).group(1, 1), (b'a', b'a'))
    for a in ('à', 'а', '𝒜'):
        self.assertEqual(re.match(a, a).groups(), ())
        self.assertEqual(re.match('(%s)' % a, a).groups(), (a,))
        self.assertEqual(re.match('(%s)' % a, a).group(0), a)
        self.assertEqual(re.match('(%s)' % a, a).group(1), a)
        self.assertEqual(re.match('(%s)' % a, a).group(1, 1), (a, a))
    pat = re.compile('((a)|(b))(c)?')
    self.assertEqual(pat.match('a').groups(), ('a', 'a', None, None))
    self.assertEqual(pat.match('b').groups(), ('b', None, 'b', None))
    self.assertEqual(pat.match('ac').groups(), ('a', 'a', None, 'c'))
    self.assertEqual(pat.match('bc').groups(), ('b', None, 'b', 'c'))
    self.assertEqual(pat.match('bc').groups(''), ('b', '', 'b', 'c'))
    pat = re.compile('(?:(?P<a1>a)|(?P<b2>b))(?P<c3>c)?')
    self.assertEqual(pat.match('a').group(1, 2, 3), ('a', None, None))
    self.assertEqual(pat.match('b').group('a1', 'b2', 'c3'), (None, 'b', None))
    self.assertEqual(pat.match('ac').group(1, 'b2', 3), ('a', None, 'c'))
