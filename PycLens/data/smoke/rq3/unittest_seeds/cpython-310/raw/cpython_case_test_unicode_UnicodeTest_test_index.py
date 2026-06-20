# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_index(self)
    self.checkequalnofix(0, 'abcdefghiabc', 'index', '')
    self.checkequalnofix(3, 'abcdefghiabc', 'index', 'def')
    self.checkequalnofix(0, 'abcdefghiabc', 'index', 'abc')
    self.checkequalnofix(9, 'abcdefghiabc', 'index', 'abc', 1)
    self.assertRaises(ValueError, 'abcdefghiabc'.index, 'hib')
    self.assertRaises(ValueError, 'abcdefghiab'.index, 'abc', 1)
    self.assertRaises(ValueError, 'abcdefghi'.index, 'ghi', 8)
    self.assertRaises(ValueError, 'abcdefghi'.index, 'ghi', -1)
    self.checkequal(100, 'Ă' * 100 + 'a', 'index', 'a')
    self.checkequal(100, '\U00100304' * 100 + 'a', 'index', 'a')
    self.checkequal(100, '\U00100304' * 100 + 'Ă', 'index', 'Ă')
    self.assertRaises(ValueError, ('a' * 100).index, 'Ă')
    self.assertRaises(ValueError, ('a' * 100).index, '\U00100304')
    self.assertRaises(ValueError, ('Ă' * 100).index, '\U00100304')
    self.checkequal(100, 'Ă' * 100 + 'a_', 'index', 'a_')
    self.checkequal(100, '\U00100304' * 100 + 'a_', 'index', 'a_')
    self.checkequal(100, '\U00100304' * 100 + 'Ă_', 'index', 'Ă_')
    self.assertRaises(ValueError, ('a' * 100).index, 'aĂ')
    self.assertRaises(ValueError, ('a' * 100).index, 'a\U00100304')
    self.assertRaises(ValueError, ('Ă' * 100).index, 'Ă\U00100304')
