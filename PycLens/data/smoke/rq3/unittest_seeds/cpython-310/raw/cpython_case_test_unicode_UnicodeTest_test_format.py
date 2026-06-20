# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(''.format(), '')
    self.assertEqual('a'.format(), 'a')
    self.assertEqual('ab'.format(), 'ab')
    self.assertEqual('a{{'.format(), 'a{')
    self.assertEqual('a}}'.format(), 'a}')
    self.assertEqual('{{b'.format(), '{b')
    self.assertEqual('}}b'.format(), '}b')
    self.assertEqual('a{{b'.format(), 'a{b')
    import datetime
    self.assertEqual('My name is {0}'.format('Fred'), 'My name is Fred')
    self.assertEqual('My name is {0[name]}'.format(dict(name='Fred')), 'My name is Fred')
    self.assertEqual('My name is {0} :-{{}}'.format('Fred'), 'My name is Fred :-{}')
    d = datetime.date(2007, 8, 18)
    self.assertEqual('The year is {0.year}'.format(d), 'The year is 2007')

    class C:

        def __init__(self, x=100):
            self._x = x

        def __format__(self, spec):
            return spec

    class D:

        def __init__(self, x):
            self.x = x

        def __format__(self, spec):
            return str(self.x)

    class E:

        def __init__(self, x):
            self.x = x

        def __str__(self):
            return 'E(' + self.x + ')'

    class F:

        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return 'F(' + self.x + ')'

    class G:

        def __init__(self, x):
            self.x = x

        def __str__(self):
            return 'string is ' + self.x

        def __format__(self, format_spec):
            if format_spec == 'd':
                return 'G(' + self.x + ')'
            return object.__format__(self, format_spec)

    class I(datetime.date):

        def __format__(self, format_spec):
            return self.strftime(format_spec)

    class J(int):

        def __format__(self, format_spec):
            return int.__format__(self * 2, format_spec)

    class M:

        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return 'M(' + self.x + ')'
        __str__ = None

    class N:

        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return 'N(' + self.x + ')'
        __format__ = None
    self.assertEqual(''.format(), '')
    self.assertEqual('abc'.format(), 'abc')
    self.assertEqual('{0}'.format('abc'), 'abc')
    self.assertEqual('{0:}'.format('abc'), 'abc')
    self.assertEqual('X{0}'.format('abc'), 'Xabc')
    self.assertEqual('{0}X'.format('abc'), 'abcX')
    self.assertEqual('X{0}Y'.format('abc'), 'XabcY')
    self.assertEqual('{1}'.format(1, 'abc'), 'abc')
    self.assertEqual('X{1}'.format(1, 'abc'), 'Xabc')
    self.assertEqual('{1}X'.format(1, 'abc'), 'abcX')
    self.assertEqual('X{1}Y'.format(1, 'abc'), 'XabcY')
    self.assertEqual('{0}'.format(-15), '-15')
    self.assertEqual('{0}{1}'.format(-15, 'abc'), '-15abc')
    self.assertEqual('{0}X{1}'.format(-15, 'abc'), '-15Xabc')
    self.assertEqual('{{'.format(), '{')
    self.assertEqual('}}'.format(), '}')
    self.assertEqual('{{}}'.format(), '{}')
    self.assertEqual('{{x}}'.format(), '{x}')
    self.assertEqual('{{{0}}}'.format(123), '{123}')
    self.assertEqual('{{{{0}}}}'.format(), '{{0}}')
    self.assertEqual('}}{{'.format(), '}{')
    self.assertEqual('}}x{{'.format(), '}x{')
    self.assertEqual('{0[foo-bar]}'.format({'foo-bar': 'baz'}), 'baz')
    self.assertEqual('{0[foo bar]}'.format({'foo bar': 'baz'}), 'baz')
    self.assertEqual('{0[ ]}'.format({' ': 3}), '3')
    self.assertEqual('{foo._x}'.format(foo=C(20)), '20')
    self.assertEqual('{1}{0}'.format(D(10), D(20)), '2010')
    self.assertEqual('{0._x.x}'.format(C(D('abc'))), 'abc')
    self.assertEqual('{0[0]}'.format(['abc', 'def']), 'abc')
    self.assertEqual('{0[1]}'.format(['abc', 'def']), 'def')
    self.assertEqual('{0[1][0]}'.format(['abc', ['def']]), 'def')
    self.assertEqual('{0[1][0].x}'.format(['abc', [D('def')]]), 'def')
    self.assertEqual('{0:.3s}'.format('abc'), 'abc')
    self.assertEqual('{0:.3s}'.format('ab'), 'ab')
    self.assertEqual('{0:.3s}'.format('abcdef'), 'abc')
    self.assertEqual('{0:.0s}'.format('abcdef'), '')
    self.assertEqual('{0:3.3s}'.format('abc'), 'abc')
    self.assertEqual('{0:2.3s}'.format('abc'), 'abc')
    self.assertEqual('{0:2.2s}'.format('abc'), 'ab')
    self.assertEqual('{0:3.2s}'.format('abc'), 'ab ')
    self.assertEqual('{0:x<0s}'.format('result'), 'result')
    self.assertEqual('{0:x<5s}'.format('result'), 'result')
    self.assertEqual('{0:x<6s}'.format('result'), 'result')
    self.assertEqual('{0:x<7s}'.format('result'), 'resultx')
    self.assertEqual('{0:x<8s}'.format('result'), 'resultxx')
    self.assertEqual('{0: <7s}'.format('result'), 'result ')
    self.assertEqual('{0:<7s}'.format('result'), 'result ')
    self.assertEqual('{0:>7s}'.format('result'), ' result')
    self.assertEqual('{0:>8s}'.format('result'), '  result')
    self.assertEqual('{0:^8s}'.format('result'), ' result ')
    self.assertEqual('{0:^9s}'.format('result'), ' result  ')
    self.assertEqual('{0:^10s}'.format('result'), '  result  ')
    self.assertEqual('{0:8s}'.format('result'), 'result  ')
    self.assertEqual('{0:0s}'.format('result'), 'result')
    self.assertEqual('{0:08s}'.format('result'), 'result00')
    self.assertEqual('{0:<08s}'.format('result'), 'result00')
    self.assertEqual('{0:>08s}'.format('result'), '00result')
    self.assertEqual('{0:^08s}'.format('result'), '0result0')
    self.assertEqual('{0:10000}'.format('a'), 'a' + ' ' * 9999)
    self.assertEqual('{0:10000}'.format(''), ' ' * 10000)
    self.assertEqual('{0:10000000}'.format(''), ' ' * 10000000)
    self.assertEqual('{0:\x00<6s}'.format('foo'), 'foo\x00\x00\x00')
    self.assertEqual('{0:\x01<6s}'.format('foo'), 'foo\x01\x01\x01')
    self.assertEqual('{0:\x00^6s}'.format('foo'), '\x00foo\x00\x00')
    self.assertEqual('{0:^6s}'.format('foo'), ' foo  ')
    self.assertEqual('{0:\x00<6}'.format(3), '3\x00\x00\x00\x00\x00')
    self.assertEqual('{0:\x01<6}'.format(3), '3\x01\x01\x01\x01\x01')
    self.assertEqual('{0:\x00^6}'.format(3), '\x00\x003\x00\x00\x00')
    self.assertEqual('{0:<6}'.format(3), '3     ')
    self.assertEqual('{0:\x00<6}'.format(3.14), '3.14\x00\x00')
    self.assertEqual('{0:\x01<6}'.format(3.14), '3.14\x01\x01')
    self.assertEqual('{0:\x00^6}'.format(3.14), '\x003.14\x00')
    self.assertEqual('{0:^6}'.format(3.14), ' 3.14 ')
    self.assertEqual('{0:\x00<12}'.format(3 + 2j), '(3+2j)\x00\x00\x00\x00\x00\x00')
    self.assertEqual('{0:\x01<12}'.format(3 + 2j), '(3+2j)\x01\x01\x01\x01\x01\x01')
    self.assertEqual('{0:\x00^12}'.format(3 + 2j), '\x00\x00\x00(3+2j)\x00\x00\x00')
    self.assertEqual('{0:^12}'.format(3 + 2j), '   (3+2j)   ')
    self.assertEqual('{0:abc}'.format(C()), 'abc')
    self.assertEqual('{0!s}'.format('Hello'), 'Hello')
    self.assertEqual('{0!s:}'.format('Hello'), 'Hello')
    self.assertEqual('{0!s:15}'.format('Hello'), 'Hello          ')
    self.assertEqual('{0!s:15s}'.format('Hello'), 'Hello          ')
    self.assertEqual('{0!r}'.format('Hello'), "'Hello'")
    self.assertEqual('{0!r:}'.format('Hello'), "'Hello'")
    self.assertEqual('{0!r}'.format(F('Hello')), 'F(Hello)')
    self.assertEqual('{0!r}'.format('\u0378'), "'\\u0378'")
    self.assertEqual('{0!r}'.format('ʹ'), "'ʹ'")
    self.assertEqual('{0!r}'.format(F('ʹ')), 'F(ʹ)')
    self.assertEqual('{0!a}'.format('Hello'), "'Hello'")
    self.assertEqual('{0!a}'.format('\u0378'), "'\\u0378'")
    self.assertEqual('{0!a}'.format('ʹ'), "'\\u0374'")
    self.assertEqual('{0!a:}'.format('Hello'), "'Hello'")
    self.assertEqual('{0!a}'.format(F('Hello')), 'F(Hello)')
    self.assertEqual('{0!a}'.format(F('ʹ')), 'F(\\u0374)')
    self.assertEqual('{0}'.format({}), '{}')
    self.assertEqual('{0}'.format([]), '[]')
    self.assertEqual('{0}'.format([1]), '[1]')
    self.assertEqual('{0:d}'.format(G('data')), 'G(data)')
    self.assertEqual('{0!s}'.format(G('data')), 'string is data')
    self.assertRaises(TypeError, '{0:^10}'.format, E('data'))
    self.assertRaises(TypeError, '{0:^10s}'.format, E('data'))
    self.assertRaises(TypeError, '{0:>15s}'.format, G('data'))
    self.assertEqual('{0:date: %Y-%m-%d}'.format(I(year=2007, month=8, day=27)), 'date: 2007-08-27')
    self.assertEqual('{0}'.format(J(10)), '20')
    self.assertEqual('{0:}'.format('a'), 'a')
    self.assertEqual('{0:.{1}}'.format('hello world', 5), 'hello')
    self.assertEqual('{0:.{1}s}'.format('hello world', 5), 'hello')
    self.assertEqual('{0:.{precision}s}'.format('hello world', precision=5), 'hello')
    self.assertEqual('{0:{width}.{precision}s}'.format('hello world', width=10, precision=5), 'hello     ')
    self.assertEqual('{0:{width}.{precision}s}'.format('hello world', width='10', precision='5'), 'hello     ')
    self.assertRaises(ValueError, '{'.format)
    self.assertRaises(ValueError, '}'.format)
    self.assertRaises(ValueError, 'a{'.format)
    self.assertRaises(ValueError, 'a}'.format)
    self.assertRaises(ValueError, '{a'.format)
    self.assertRaises(ValueError, '}a'.format)
    self.assertRaises(IndexError, '{0}'.format)
    self.assertRaises(IndexError, '{1}'.format, 'abc')
    self.assertRaises(KeyError, '{x}'.format)
    self.assertRaises(ValueError, '}{'.format)
    self.assertRaises(ValueError, 'abc{0:{}'.format)
    self.assertRaises(ValueError, '{0'.format)
    self.assertRaises(IndexError, '{0.}'.format)
    self.assertRaises(ValueError, '{0.}'.format, 0)
    self.assertRaises(ValueError, '{0[}'.format)
    self.assertRaises(ValueError, '{0[}'.format, [])
    self.assertRaises(KeyError, '{0]}'.format)
    self.assertRaises(ValueError, '{0.[]}'.format, 0)
    self.assertRaises(ValueError, '{0..foo}'.format, 0)
    self.assertRaises(ValueError, '{0[0}'.format, 0)
    self.assertRaises(ValueError, '{0[0:foo}'.format, 0)
    self.assertRaises(KeyError, '{c]}'.format)
    self.assertRaises(ValueError, '{{ {{{0}}'.format, 0)
    self.assertRaises(ValueError, '{0}}'.format, 0)
    self.assertRaises(KeyError, '{foo}'.format, bar=3)
    self.assertRaises(ValueError, '{0!x}'.format, 3)
    self.assertRaises(ValueError, '{0!}'.format, 0)
    self.assertRaises(ValueError, '{0!rs}'.format, 0)
    self.assertRaises(ValueError, '{!}'.format)
    self.assertRaises(IndexError, '{:}'.format)
    self.assertRaises(IndexError, '{:s}'.format)
    self.assertRaises(IndexError, '{}'.format)
    big = '23098475029384702983476098230754973209482573'
    self.assertRaises(ValueError, ('{' + big + '}').format)
    self.assertRaises(ValueError, ('{[' + big + ']}').format, [0])
    self.assertRaises(ValueError, '{0:x}'.format, 1j)
    self.assertRaises(ValueError, '{0:x}'.format, 1.0)
    self.assertRaises(ValueError, '{0:X}'.format, 1j)
    self.assertRaises(ValueError, '{0:X}'.format, 1.0)
    self.assertRaises(ValueError, '{0:o}'.format, 1j)
    self.assertRaises(ValueError, '{0:o}'.format, 1.0)
    self.assertRaises(ValueError, '{0:u}'.format, 1j)
    self.assertRaises(ValueError, '{0:u}'.format, 1.0)
    self.assertRaises(ValueError, '{0:i}'.format, 1j)
    self.assertRaises(ValueError, '{0:i}'.format, 1.0)
    self.assertRaises(ValueError, '{0:d}'.format, 1j)
    self.assertRaises(ValueError, '{0:d}'.format, 1.0)
    self.assertRaises(ValueError, '{0[0]x}'.format, [None])
    self.assertRaises(ValueError, '{0[0](10)}'.format, [None])
    self.assertRaises(TypeError, '{0[{1}]}'.format, 'abcdefg', 4)
    self.assertRaises(ValueError, '{0:{1:{2}}}'.format, 'abc', 's', '')
    self.assertRaises(ValueError, '{0:{1:{2:{3:{4:{5:{6}}}}}}}'.format, 0, 1, 2, 3, 4, 5, 6, 7)
    sign_msg = 'Sign not allowed in string format specifier'
    self.assertRaisesRegex(ValueError, sign_msg, '{0:-s}'.format, '')
    self.assertRaisesRegex(ValueError, sign_msg, format, '', '-')
    space_msg = 'Space not allowed in string format specifier'
    self.assertRaisesRegex(ValueError, space_msg, '{: }'.format, '')
    self.assertRaises(ValueError, '{0:=s}'.format, '')
    self.assertRaises(ValueError, format, '', '#')
    self.assertRaises(ValueError, format, '', '#20')
    self.assertEqual('{0:s}{1:s}'.format('ABC', 'АБВ'), 'ABCАБВ')
    self.assertEqual('{0:.3s}'.format('ABCАБВ'), 'ABC')
    self.assertEqual('{0:.0s}'.format('ABCАБВ'), '')
    self.assertEqual('{[{}]}'.format({'{}': 5}), '5')
    self.assertEqual('{[{}]}'.format({'{}': 'a'}), 'a')
    self.assertEqual('{[{]}'.format({'{': 'a'}), 'a')
    self.assertEqual('{[}]}'.format({'}': 'a'}), 'a')
    self.assertEqual('{[[]}'.format({'[': 'a'}), 'a')
    self.assertEqual('{[!]}'.format({'!': 'a'}), 'a')
    self.assertRaises(ValueError, '{a{}b}'.format, 42)
    self.assertRaises(ValueError, '{a{b}'.format, 42)
    self.assertRaises(ValueError, '{[}'.format, 42)
    self.assertEqual('0x{:0{:d}X}'.format(0, 16), '0x0000000000000000')
    m = M('data')
    self.assertEqual('{!r}'.format(m), 'M(data)')
    self.assertRaises(TypeError, '{!s}'.format, m)
    self.assertRaises(TypeError, '{}'.format, m)
    n = N('data')
    self.assertEqual('{!r}'.format(n), 'N(data)')
    self.assertEqual('{!s}'.format(n), 'N(data)')
    self.assertRaises(TypeError, '{}'.format, n)
