# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isnumeric

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkequalnofix(False, '', 'isnumeric')
    self.checkequalnofix(False, 'a', 'isnumeric')
    self.checkequalnofix(True, '0', 'isnumeric')
    self.checkequalnofix(True, '①', 'isnumeric')
    self.checkequalnofix(True, '¼', 'isnumeric')
    self.checkequalnofix(True, '٠', 'isnumeric')
    self.checkequalnofix(True, '0123456789', 'isnumeric')
    self.checkequalnofix(False, '0123456789a', 'isnumeric')
    self.assertRaises(TypeError, 'abc'.isnumeric, 42)
    for ch in ['𐐁', '𐐧', '𐐩', '𐑎', '🐍', '👯']:
        self.assertFalse(ch.isnumeric(), '{!a} is not numeric.'.format(ch))
    for ch in ['𑁥', '𝟶', '𑁦', '𐒠', '🄇']:
        self.assertTrue(ch.isnumeric(), '{!a} is numeric.'.format(ch))
