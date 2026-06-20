# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isalpha

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_isalpha()
    self.checkequalnofix(True, 'ῼ', 'isalpha')
    self.assertTrue('𐐁'.isalpha())
    self.assertTrue('𐐧'.isalpha())
    self.assertTrue('𐐩'.isalpha())
    self.assertTrue('𐑎'.isalpha())
    self.assertFalse('🐍'.isalpha())
    self.assertFalse('👯'.isalpha())
