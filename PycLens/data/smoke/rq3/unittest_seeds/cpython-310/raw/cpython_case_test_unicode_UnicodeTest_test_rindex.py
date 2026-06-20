# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_rindex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_rindex(self)
    self.checkequalnofix(12, 'abcdefghiabc', 'rindex', '')
    self.checkequalnofix(3, 'abcdefghiabc', 'rindex', 'def')
    self.checkequalnofix(9, 'abcdefghiabc', 'rindex', 'abc')
    self.checkequalnofix(0, 'abcdefghiabc', 'rindex', 'abc', 0, -1)
    self.assertRaises(ValueError, 'abcdefghiabc'.rindex, 'hib')
    self.assertRaises(ValueError, 'defghiabc'.rindex, 'def', 1)
    self.assertRaises(ValueError, 'defghiabc'.rindex, 'abc', 0, -1)
    self.assertRaises(ValueError, 'abcdefghi'.rindex, 'ghi', 0, 8)
    self.assertRaises(ValueError, 'abcdefghi'.rindex, 'ghi', 0, -1)
    self.checkequal(0, 'a' + 'Ă' * 100, 'rindex', 'a')
    self.checkequal(0, 'a' + '\U00100304' * 100, 'rindex', 'a')
    self.checkequal(0, 'Ă' + '\U00100304' * 100, 'rindex', 'Ă')
    self.assertRaises(ValueError, ('a' * 100).rindex, 'Ă')
    self.assertRaises(ValueError, ('a' * 100).rindex, '\U00100304')
    self.assertRaises(ValueError, ('Ă' * 100).rindex, '\U00100304')
    self.checkequal(0, '_a' + 'Ă' * 100, 'rindex', '_a')
    self.checkequal(0, '_a' + '\U00100304' * 100, 'rindex', '_a')
    self.checkequal(0, '_Ă' + '\U00100304' * 100, 'rindex', '_Ă')
    self.assertRaises(ValueError, ('a' * 100).rindex, 'Ăa')
    self.assertRaises(ValueError, ('a' * 100).rindex, '\U00100304a')
    self.assertRaises(ValueError, ('Ă' * 100).rindex, '\U00100304Ă')
