# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for string in (':a:b::c', S(':a:b::c')):
        self.assertTypedEqual(re.split(':', string), ['', 'a', 'b', '', 'c'])
        self.assertTypedEqual(re.split(':+', string), ['', 'a', 'b', 'c'])
        self.assertTypedEqual(re.split('(:+)', string), ['', ':', 'a', ':', 'b', '::', 'c'])
    for string in (b':a:b::c', B(b':a:b::c'), bytearray(b':a:b::c'), memoryview(b':a:b::c')):
        self.assertTypedEqual(re.split(b':', string), [b'', b'a', b'b', b'', b'c'])
        self.assertTypedEqual(re.split(b':+', string), [b'', b'a', b'b', b'c'])
        self.assertTypedEqual(re.split(b'(:+)', string), [b'', b':', b'a', b':', b'b', b'::', b'c'])
    for (a, b, c) in ('àßç', 'абв', '𝒜𝒞𝒵'):
        string = ':%s:%s::%s' % (a, b, c)
        self.assertEqual(re.split(':', string), ['', a, b, '', c])
        self.assertEqual(re.split(':+', string), ['', a, b, c])
        self.assertEqual(re.split('(:+)', string), ['', ':', a, ':', b, '::', c])
    self.assertEqual(re.split('(?::+)', ':a:b::c'), ['', 'a', 'b', 'c'])
    self.assertEqual(re.split('(:)+', ':a:b::c'), ['', ':', 'a', ':', 'b', ':', 'c'])
    self.assertEqual(re.split('([b:]+)', ':a:b::c'), ['', ':', 'a', ':b::', 'c'])
    self.assertEqual(re.split('(b)|(:+)', ':a:b::c'), ['', None, ':', 'a', None, ':', '', 'b', None, '', None, '::', 'c'])
    self.assertEqual(re.split('(?:b)|(?::+)', ':a:b::c'), ['', 'a', '', '', 'c'])
    for (sep, expected) in [(':*', ['', '', 'a', '', 'b', '', 'c', '']), ('(?::*)', ['', '', 'a', '', 'b', '', 'c', '']), ('(:*)', ['', ':', '', '', 'a', ':', '', '', 'b', '::', '', '', 'c', '', '']), ('(:)*', ['', ':', '', None, 'a', ':', '', None, 'b', ':', '', None, 'c', None, ''])]:
        with self.subTest(sep=sep):
            self.assertTypedEqual(re.split(sep, ':a:b::c'), expected)
    for (sep, expected) in [('', ['', ':', 'a', ':', 'b', ':', ':', 'c', '']), ('\\b', [':', 'a', ':', 'b', '::', 'c', '']), ('(?=:)', ['', ':a', ':b', ':', ':c']), ('(?<=:)', [':', 'a:', 'b:', ':', 'c'])]:
        with self.subTest(sep=sep):
            self.assertTypedEqual(re.split(sep, ':a:b::c'), expected)
