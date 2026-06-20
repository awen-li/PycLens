# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_islower

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_islower()
    self.checkequalnofix(False, 'ῼ', 'islower')
    self.assertFalse('Ⅷ'.islower())
    self.assertTrue('ⅷ'.islower())
    self.assertFalse('𐐁'.islower())
    self.assertFalse('𐐧'.islower())
    self.assertTrue('𐐩'.islower())
    self.assertTrue('𐑎'.islower())
    self.assertFalse('🐍'.islower())
    self.assertFalse('👯'.islower())
