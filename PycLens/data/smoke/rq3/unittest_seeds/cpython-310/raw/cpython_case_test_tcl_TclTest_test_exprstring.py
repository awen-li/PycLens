# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_exprstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp
    tcl.call('set', 'a', 3)
    tcl.call('set', 'b', 6)

    def check(expr, expected):
        result = tcl.exprstring(expr)
        self.assertEqual(result, expected)
        self.assertIsInstance(result, str)
    self.assertRaises(TypeError, tcl.exprstring)
    self.assertRaises(TypeError, tcl.exprstring, '8.2', '+6')
    self.assertRaises(TypeError, tcl.exprstring, b'8.2 + 6')
    self.assertRaises(TclError, tcl.exprstring, 'spam')
    check('', '0')
    check('8.2 + 6', '14.2')
    check('3.1 + $a', '6.1')
    check('2 + "$a.$b"', '5.6')
    check('4*[llength "6 2"]', '8')
    check('{word one} < "word $a"', '0')
    check('4*2 < 7', '0')
    check('hypot($a, 4)', '5.0')
    check('5 / 4', '1')
    check('5 / 4.0', '1.25')
    check('5 / ( [string length "abcd"] + 0.0 )', '1.25')
    check('20.0/5.0', '4.0')
    check('"0x03" > "2"', '1')
    check('[string length "a½€"]', '3')
    check('[string length "a\\xbd\\u20ac"]', '3')
    check('"abc"', 'abc')
    check('"a½€"', 'a½€')
    check('"a\\xbd\\u20ac"', 'a½€')
    check('"a\\0b"', 'a\x00b')
    if tcl_version >= (8, 5):
        check('2**64', str(2 ** 64))
