# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isdigit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_isdigit()
    self.checkequalnofix(True, '①', 'isdigit')
    self.checkequalnofix(False, '¼', 'isdigit')
    self.checkequalnofix(True, '٠', 'isdigit')
    for ch in ['𐐁', '𐐧', '𐐩', '𐑎', '🐍', '👯', '𑁥']:
        self.assertFalse(ch.isdigit(), '{!a} is not a digit.'.format(ch))
    for ch in ['𝟶', '𑁦', '𐒠', '🄇']:
        self.assertTrue(ch.isdigit(), '{!a} is a digit.'.format(ch))
