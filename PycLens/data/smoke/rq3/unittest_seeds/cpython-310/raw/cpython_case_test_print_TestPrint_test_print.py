# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_print.py
# case: TestPrint_test_print

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def x(expected, args, sep=NotDefined, end=NotDefined):
        self.check(expected, args, sep=sep, end=end)
        o = StringIO()
        self.check('', args, sep=sep, end=end, file=o)
        self.assertEqual(o.getvalue(), expected)
    x('\n', ())
    x('a\n', ('a',))
    x('None\n', (None,))
    x('1 2\n', (1, 2))
    x('1   2\n', (1, ' ', 2))
    x('1*2\n', (1, 2), sep='*')
    x('1 s', (1, 's'), end='')
    x('a\nb\n', ('a', 'b'), sep='\n')
    x('1.01', (1.0, 1), sep='', end='')
    x('1*a*1.3+', (1, 'a', 1.3), sep='*', end='+')
    x('a\n\nb\n', ('a\n', 'b'), sep='\n')
    x('\x00+ +\x00\n', ('\x00', ' ', '\x00'), sep='+')
    x('a\n b\n', ('a\n', 'b'))
    x('a\n b\n', ('a\n', 'b'), sep=None)
    x('a\n b\n', ('a\n', 'b'), end=None)
    x('a\n b\n', ('a\n', 'b'), sep=None, end=None)
    x('*\n', (ClassWith__str__('*'),))
    x('abc 1\n', (ClassWith__str__('abc'), 1))
    self.assertRaises(TypeError, print, '', sep=3)
    self.assertRaises(TypeError, print, '', end=3)
    self.assertRaises(AttributeError, print, '', file='')
