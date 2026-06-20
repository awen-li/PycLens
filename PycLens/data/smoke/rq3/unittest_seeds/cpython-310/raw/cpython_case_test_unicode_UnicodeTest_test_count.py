# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_count(self)
    self.checkequalnofix(3, 'aaa', 'count', 'a')
    self.checkequalnofix(0, 'aaa', 'count', 'b')
    self.checkequalnofix(3, 'aaa', 'count', 'a')
    self.checkequalnofix(0, 'aaa', 'count', 'b')
    self.checkequalnofix(0, 'aaa', 'count', 'b')
    self.checkequalnofix(1, 'aaa', 'count', 'a', -1)
    self.checkequalnofix(3, 'aaa', 'count', 'a', -10)
    self.checkequalnofix(2, 'aaa', 'count', 'a', 0, -1)
    self.checkequalnofix(0, 'aaa', 'count', 'a', 0, -10)
    self.checkequal(10, 'Ă' + 'a' * 10, 'count', 'a')
    self.checkequal(10, '\U00100304' + 'a' * 10, 'count', 'a')
    self.checkequal(10, '\U00100304' + 'Ă' * 10, 'count', 'Ă')
    self.checkequal(0, 'a' * 10, 'count', 'Ă')
    self.checkequal(0, 'a' * 10, 'count', '\U00100304')
    self.checkequal(0, 'Ă' * 10, 'count', '\U00100304')
    self.checkequal(10, 'Ă' + 'a_' * 10, 'count', 'a_')
    self.checkequal(10, '\U00100304' + 'a_' * 10, 'count', 'a_')
    self.checkequal(10, '\U00100304' + 'Ă_' * 10, 'count', 'Ă_')
    self.checkequal(0, 'a' * 10, 'count', 'aĂ')
    self.checkequal(0, 'a' * 10, 'count', 'a\U00100304')
    self.checkequal(0, 'Ă' * 10, 'count', 'Ă\U00100304')
