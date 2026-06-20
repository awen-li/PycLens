# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isspace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_isspace()
    self.checkequalnofix(True, '\u2000', 'isspace')
    self.checkequalnofix(True, '\u200a', 'isspace')
    self.checkequalnofix(False, '—', 'isspace')
    for ch in ['𐐁', '𐐧', '𐐩', '𐑎', '🐍', '👯']:
        self.assertFalse(ch.isspace(), '{!a} is not space.'.format(ch))
