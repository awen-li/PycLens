# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isupper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_isupper()
    if not sys.platform.startswith('java'):
        self.checkequalnofix(False, 'ῼ', 'isupper')
    self.assertTrue('Ⅷ'.isupper())
    self.assertFalse('ⅷ'.isupper())
    self.assertTrue('𐐁'.isupper())
    self.assertTrue('𐐧'.isupper())
    self.assertFalse('𐐩'.isupper())
    self.assertFalse('𐑎'.isupper())
    self.assertFalse('🐍'.isupper())
    self.assertFalse('👯'.isupper())
