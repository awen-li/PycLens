# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_basic_re_sub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTypedEqual(re.sub('y', 'a', 'xyz'), 'xaz')
    self.assertTypedEqual(re.sub('y', S('a'), S('xyz')), 'xaz')
    self.assertTypedEqual(re.sub(b'y', b'a', b'xyz'), b'xaz')
    self.assertTypedEqual(re.sub(b'y', B(b'a'), B(b'xyz')), b'xaz')
    self.assertTypedEqual(re.sub(b'y', bytearray(b'a'), bytearray(b'xyz')), b'xaz')
    self.assertTypedEqual(re.sub(b'y', memoryview(b'a'), memoryview(b'xyz')), b'xaz')
    for y in ('à', 'а', '𝒜'):
        self.assertEqual(re.sub(y, 'a', 'x%sz' % y), 'xaz')
    self.assertEqual(re.sub('(?i)b+', 'x', 'bbbb BBBB'), 'x x')
    self.assertEqual(re.sub('\\d+', self.bump_num, '08.2 -2 23x99y'), '9.3 -3 24x100y')
    self.assertEqual(re.sub('\\d+', self.bump_num, '08.2 -2 23x99y', 3), '9.3 -3 23x99y')
    self.assertEqual(re.sub('\\d+', self.bump_num, '08.2 -2 23x99y', count=3), '9.3 -3 23x99y')
    self.assertEqual(re.sub('.', lambda m: '\\n', 'x'), '\\n')
    self.assertEqual(re.sub('.', '\\n', 'x'), '\n')
    s = '\\1\\1'
    self.assertEqual(re.sub('(.)', s, 'x'), 'xx')
    self.assertEqual(re.sub('(.)', s.replace('\\', '\\\\'), 'x'), s)
    self.assertEqual(re.sub('(.)', lambda m: s, 'x'), s)
    self.assertEqual(re.sub('(?P<a>x)', '\\g<a>\\g<a>', 'xx'), 'xxxx')
    self.assertEqual(re.sub('(?P<a>x)', '\\g<a>\\g<1>', 'xx'), 'xxxx')
    self.assertEqual(re.sub('(?P<unk>x)', '\\g<unk>\\g<unk>', 'xx'), 'xxxx')
    self.assertEqual(re.sub('(?P<unk>x)', '\\g<1>\\g<1>', 'xx'), 'xxxx')
    self.assertEqual(re.sub('a', '\\t\\n\\v\\r\\f\\a\\b', 'a'), '\t\n\x0b\r\x0c\x07\x08')
    self.assertEqual(re.sub('a', '\t\n\x0b\r\x0c\x07\x08', 'a'), '\t\n\x0b\r\x0c\x07\x08')
    self.assertEqual(re.sub('a', '\t\n\x0b\r\x0c\x07\x08', 'a'), chr(9) + chr(10) + chr(11) + chr(13) + chr(12) + chr(7) + chr(8))
    for c in 'cdehijklmopqsuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        with self.subTest(c):
            with self.assertRaises(re.error):
                self.assertEqual(re.sub('a', '\\' + c, 'a'), '\\' + c)
    self.assertEqual(re.sub('^\\s*', 'X', 'test'), 'Xtest')
