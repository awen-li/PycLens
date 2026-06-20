# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isprintable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(''.isprintable())
    self.assertTrue(' '.isprintable())
    self.assertTrue('abcdefg'.isprintable())
    self.assertFalse('abcdefg\n'.isprintable())
    self.assertTrue('ʹ'.isprintable())
    self.assertFalse('\u0378'.isprintable())
    self.assertFalse('\ud800'.isprintable())
    self.assertTrue('👯'.isprintable())
    self.assertFalse('\U000e0020'.isprintable())
