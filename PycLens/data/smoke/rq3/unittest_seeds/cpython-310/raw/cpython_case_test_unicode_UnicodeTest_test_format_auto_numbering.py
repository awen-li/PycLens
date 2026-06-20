# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_format_auto_numbering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, x=100):
            self._x = x

        def __format__(self, spec):
            return spec
    self.assertEqual('{}'.format(10), '10')
    self.assertEqual('{:5}'.format('s'), 's    ')
    self.assertEqual('{!r}'.format('s'), "'s'")
    self.assertEqual('{._x}'.format(C(10)), '10')
    self.assertEqual('{[1]}'.format([1, 2]), '2')
    self.assertEqual('{[a]}'.format({'a': 4, 'b': 2}), '4')
    self.assertEqual('a{}b{}c'.format(0, 1), 'a0b1c')
    self.assertEqual('a{:{}}b'.format('x', '^10'), 'a    x     b')
    self.assertEqual('a{:{}x}b'.format(20, '#'), 'a0x14b')
    self.assertRaises(ValueError, '{}{1}'.format, 1, 2)
    self.assertRaises(ValueError, '{1}{}'.format, 1, 2)
    self.assertRaises(ValueError, '{:{1}}'.format, 1, 2)
    self.assertRaises(ValueError, '{0:{}}'.format, 1, 2)
    self.assertEqual('{f}{}'.format(4, f='test'), 'test4')
    self.assertEqual('{}{f}'.format(4, f='test'), '4test')
    self.assertEqual('{:{f}}{g}{}'.format(1, 3, g='g', f=2), ' 1g3')
    self.assertEqual('{f:{}}{}{g}'.format(2, 4, f=1, g='g'), ' 14g')
