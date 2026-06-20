# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_plain_integers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(type(0), type(0))
    self.assertEqual(255, 255)
    self.assertEqual(255, 255)
    self.assertEqual(2147483647, 2147483647)
    self.assertEqual(9, 9)
    self.assertRaises(SyntaxError, eval, '0x')
    from sys import maxsize
    if maxsize == 2147483647:
        self.assertEqual(-2147483647 - 1, -2147483648)
        self.assertTrue(4294967295 > 0)
        self.assertTrue(4294967295 > 0)
        self.assertTrue(2147483647 > 0)
        for s in ('2147483648', '0o40000000000', '0x100000000', '0b10000000000000000000000000000000'):
            try:
                x = eval(s)
            except OverflowError:
                self.fail('OverflowError on huge integer literal %r' % s)
    elif maxsize == 9223372036854775807:
        self.assertEqual(-9223372036854775807 - 1, -9223372036854775808)
        self.assertTrue(18446744073709551615 > 0)
        self.assertTrue(18446744073709551615 > 0)
        self.assertTrue(4611686018427387903 > 0)
        for s in ('9223372036854775808', '0o2000000000000000000000', '0x10000000000000000', '0b100000000000000000000000000000000000000000000000000000000000000'):
            try:
                x = eval(s)
            except OverflowError:
                self.fail('OverflowError on huge integer literal %r' % s)
    else:
        self.fail('Weird maxsize value %r' % maxsize)
