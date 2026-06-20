# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isdecimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkequalnofix(False, '', 'isdecimal')
    self.checkequalnofix(False, 'a', 'isdecimal')
    self.checkequalnofix(True, '0', 'isdecimal')
    self.checkequalnofix(False, '①', 'isdecimal')
    self.checkequalnofix(False, '¼', 'isdecimal')
    self.checkequalnofix(True, '٠', 'isdecimal')
    self.checkequalnofix(True, '0123456789', 'isdecimal')
    self.checkequalnofix(False, '0123456789a', 'isdecimal')
    self.checkraises(TypeError, 'abc', 'isdecimal', 42)
    for ch in ['𐐁', '𐐧', '𐐩', '𐑎', '🐍', '👯', '𑁥', '🄇']:
        self.assertFalse(ch.isdecimal(), '{!a} is not decimal.'.format(ch))
    for ch in ['𝟶', '𑁦', '𐒠']:
        self.assertTrue(ch.isdecimal(), '{!a} is decimal.'.format(ch))
