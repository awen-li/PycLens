# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_exprboolean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp
    tcl.call('set', 'a', 3)
    tcl.call('set', 'b', 6)

    def check(expr, expected):
        result = tcl.exprboolean(expr)
        self.assertEqual(result, expected)
        self.assertIsInstance(result, int)
        self.assertNotIsInstance(result, bool)
    self.assertRaises(TypeError, tcl.exprboolean)
    self.assertRaises(TypeError, tcl.exprboolean, '8.2', '+6')
    self.assertRaises(TypeError, tcl.exprboolean, b'8.2 + 6')
    self.assertRaises(TclError, tcl.exprboolean, 'spam')
    check('', False)
    for value in ('0', 'false', 'no', 'off'):
        check(value, False)
        check('"%s"' % value, False)
        check('{%s}' % value, False)
    for value in ('1', 'true', 'yes', 'on'):
        check(value, True)
        check('"%s"' % value, True)
        check('{%s}' % value, True)
    check('8.2 + 6', True)
    check('3.1 + $a', True)
    check('2 + "$a.$b"', True)
    check('4*[llength "6 2"]', True)
    check('{word one} < "word $a"', False)
    check('4*2 < 7', False)
    check('hypot($a, 4)', True)
    check('5 / 4', True)
    check('5 / 4.0', True)
    check('5 / ( [string length "abcd"] + 0.0 )', True)
    check('20.0/5.0', True)
    check('"0x03" > "2"', True)
    check('[string length "a½€"]', True)
    check('[string length "a\\xbd\\u20ac"]', True)
    self.assertRaises(TclError, tcl.exprboolean, '"abc"')
    if tcl_version >= (8, 5):
        check('2**64', True)
