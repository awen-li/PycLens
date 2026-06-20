# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.MixinStrUnicodeUserStringTest.test_formatting(self)
    self.assertEqual('%s, %s' % ('abc', 'abc'), 'abc, abc')
    self.assertEqual('%s, %s, %i, %f, %5.2f' % ('abc', 'abc', 1, 2, 3), 'abc, abc, 1, 2.000000,  3.00')
    self.assertEqual('%s, %s, %i, %f, %5.2f' % ('abc', 'abc', 1, -2, 3), 'abc, abc, 1, -2.000000,  3.00')
    self.assertEqual('%s, %s, %i, %f, %5.2f' % ('abc', 'abc', -1, -2, 3.5), 'abc, abc, -1, -2.000000,  3.50')
    self.assertEqual('%s, %s, %i, %f, %5.2f' % ('abc', 'abc', -1, -2, 3.57), 'abc, abc, -1, -2.000000,  3.57')
    self.assertEqual('%s, %s, %i, %f, %5.2f' % ('abc', 'abc', -1, -2, 1003.57), 'abc, abc, -1, -2.000000, 1003.57')
    if not sys.platform.startswith('java'):
        self.assertEqual('%r, %r' % (b'abc', 'abc'), "b'abc', 'abc'")
        self.assertEqual('%r' % ('ሴ',), "'ሴ'")
        self.assertEqual('%a' % ('ሴ',), "'\\u1234'")
    self.assertEqual('%(x)s, %(y)s' % {'x': 'abc', 'y': 'def'}, 'abc, def')
    self.assertEqual('%(x)s, %(ü)s' % {'x': 'abc', 'ü': 'def'}, 'abc, def')
    self.assertEqual('%c' % 4660, 'ሴ')
    self.assertEqual('%c' % 136323, '𡒃')
    self.assertRaises(OverflowError, '%c'.__mod__, (1114112,))
    self.assertEqual('%c' % '𡒃', '𡒃')
    self.assertRaises(TypeError, '%c'.__mod__, 'aa')
    self.assertRaises(ValueError, '%.1ဲf'.__mod__, 1.0 / 3)
    self.assertRaises(TypeError, '%i'.__mod__, 'aa')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc'}, '...abc...')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc'}, '...abc...')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc'}, '...abc...')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc'}, '...abc...')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc', 'def': 123}, '...abc...')
    self.assertEqual('...%(foo)s...' % {'foo': 'abc', 'def': 123}, '...abc...')
    self.assertEqual('...%s...%s...%s...%s...' % (1, 2, 3, 'abc'), '...1...2...3...abc...')
    self.assertEqual('...%%...%%s...%s...%s...%s...%s...' % (1, 2, 3, 'abc'), '...%...%s...1...2...3...abc...')
    self.assertEqual('...%s...' % 'abc', '...abc...')
    self.assertEqual('%*s' % (5, 'abc'), '  abc')
    self.assertEqual('%*s' % (-5, 'abc'), 'abc  ')
    self.assertEqual('%*.*s' % (5, 2, 'abc'), '   ab')
    self.assertEqual('%*.*s' % (5, 3, 'abc'), '  abc')
    self.assertEqual('%i %*.*s' % (10, 5, 3, 'abc'), '10   abc')
    self.assertEqual('%i%s %*.*s' % (10, 3, 5, 3, 'abc'), '103   abc')
    self.assertEqual('%c' % 'a', 'a')

    class Wrapper:

        def __str__(self):
            return 'ሴ'
    self.assertEqual('%s' % Wrapper(), 'ሴ')
    NAN = float('nan')
    INF = float('inf')
    self.assertEqual('%f' % NAN, 'nan')
    self.assertEqual('%F' % NAN, 'NAN')
    self.assertEqual('%f' % INF, 'inf')
    self.assertEqual('%F' % INF, 'INF')
    self.assertEqual('%.1s' % 'aé€', 'a')
    self.assertEqual('%.2s' % 'aé€', 'aé')

    class PseudoInt:

        def __init__(self, value):
            self.value = int(value)

        def __int__(self):
            return self.value

        def __index__(self):
            return self.value

    class PseudoFloat:

        def __init__(self, value):
            self.value = float(value)

        def __int__(self):
            return int(self.value)
    pi = PseudoFloat(3.1415)
    letter_m = PseudoInt(109)
    self.assertEqual('%x' % 42, '2a')
    self.assertEqual('%X' % 15, 'F')
    self.assertEqual('%o' % 9, '11')
    self.assertEqual('%c' % 109, 'm')
    self.assertEqual('%x' % letter_m, '6d')
    self.assertEqual('%X' % letter_m, '6D')
    self.assertEqual('%o' % letter_m, '155')
    self.assertEqual('%c' % letter_m, 'm')
    self.assertRaisesRegex(TypeError, '%x format: an integer is required, not float', operator.mod, '%x', 3.14)
    self.assertRaisesRegex(TypeError, '%X format: an integer is required, not float', operator.mod, '%X', 2.11)
    self.assertRaisesRegex(TypeError, '%o format: an integer is required, not float', operator.mod, '%o', 1.79)
    self.assertRaisesRegex(TypeError, '%x format: an integer is required, not PseudoFloat', operator.mod, '%x', pi)
    self.assertRaisesRegex(TypeError, '%x format: an integer is required, not complex', operator.mod, '%x', 3j)
    self.assertRaisesRegex(TypeError, '%X format: an integer is required, not complex', operator.mod, '%X', 2j)
    self.assertRaisesRegex(TypeError, '%o format: an integer is required, not complex', operator.mod, '%o', 1j)
    self.assertRaisesRegex(TypeError, '%u format: a real number is required, not complex', operator.mod, '%u', 3j)
    self.assertRaisesRegex(TypeError, '%i format: a real number is required, not complex', operator.mod, '%i', 2j)
    self.assertRaisesRegex(TypeError, '%d format: a real number is required, not complex', operator.mod, '%d', 1j)
    self.assertRaisesRegex(TypeError, '%c requires int or char', operator.mod, '%c', pi)

    class RaisingNumber:

        def __int__(self):
            raise RuntimeError('int')

        def __index__(self):
            raise RuntimeError('index')
    rn = RaisingNumber()
    self.assertRaisesRegex(RuntimeError, 'int', operator.mod, '%d', rn)
    self.assertRaisesRegex(RuntimeError, 'int', operator.mod, '%i', rn)
    self.assertRaisesRegex(RuntimeError, 'int', operator.mod, '%u', rn)
    self.assertRaisesRegex(RuntimeError, 'index', operator.mod, '%x', rn)
    self.assertRaisesRegex(RuntimeError, 'index', operator.mod, '%X', rn)
    self.assertRaisesRegex(RuntimeError, 'index', operator.mod, '%o', rn)
