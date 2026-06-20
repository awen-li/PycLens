# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_upper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_upper(self)
    self.assertEqual('𐑏'.upper(), '𐐧')
    self.assertEqual('𐑏𐑏'.upper(), '𐐧𐐧')
    self.assertEqual('𐐧𐑏'.upper(), '𐐧𐐧')
    self.assertEqual('X𐐧x𐑏'.upper(), 'X𐐧X𐐧')
    self.assertEqual('ﬁ'.upper(), 'FI')
    self.assertEqual('İ'.upper(), 'İ')
    self.assertEqual('Σ'.upper(), 'Σ')
    self.assertEqual('ß'.upper(), 'SS')
    self.assertEqual('ῒ'.upper(), 'Ϊ̀')
    self.assertEqual('\U0008fffe'.upper(), '\U0008fffe')
    self.assertEqual('ⅷ'.upper(), 'Ⅷ')
