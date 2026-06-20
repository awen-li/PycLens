# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_findall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.findall(':+', 'abc'), [])
    for string in ('a:b::c:::d', S('a:b::c:::d')):
        self.assertTypedEqual(re.findall(':+', string), [':', '::', ':::'])
        self.assertTypedEqual(re.findall('(:+)', string), [':', '::', ':::'])
        self.assertTypedEqual(re.findall('(:)(:*)', string), [(':', ''), (':', ':'), (':', '::')])
    for string in (b'a:b::c:::d', B(b'a:b::c:::d'), bytearray(b'a:b::c:::d'), memoryview(b'a:b::c:::d')):
        self.assertTypedEqual(re.findall(b':+', string), [b':', b'::', b':::'])
        self.assertTypedEqual(re.findall(b'(:+)', string), [b':', b'::', b':::'])
        self.assertTypedEqual(re.findall(b'(:)(:*)', string), [(b':', b''), (b':', b':'), (b':', b'::')])
    for x in ('à', 'а', '𝒜'):
        xx = x * 2
        xxx = x * 3
        string = 'a%sb%sc%sd' % (x, xx, xxx)
        self.assertEqual(re.findall('%s+' % x, string), [x, xx, xxx])
        self.assertEqual(re.findall('(%s+)' % x, string), [x, xx, xxx])
        self.assertEqual(re.findall('(%s)(%s*)' % (x, x), string), [(x, ''), (x, x), (x, xx)])
