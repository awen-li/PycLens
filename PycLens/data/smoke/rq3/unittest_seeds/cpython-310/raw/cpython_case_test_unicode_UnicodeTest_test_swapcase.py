# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_swapcase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_swapcase(self)
    self.assertEqual('𐑏'.swapcase(), '𐐧')
    self.assertEqual('𐐧'.swapcase(), '𐑏')
    self.assertEqual('𐑏𐑏'.swapcase(), '𐐧𐐧')
    self.assertEqual('𐐧𐑏'.swapcase(), '𐑏𐐧')
    self.assertEqual('𐑏𐐧'.swapcase(), '𐐧𐑏')
    self.assertEqual('X𐐧x𐑏'.swapcase(), 'x𐑏X𐐧')
    self.assertEqual('ﬁ'.swapcase(), 'FI')
    self.assertEqual('İ'.swapcase(), 'i̇')
    self.assertEqual('Σ'.swapcase(), 'σ')
    self.assertEqual('ͅΣ'.swapcase(), 'Ισ')
    self.assertEqual('AͅΣ'.swapcase(), 'aΙς')
    self.assertEqual('AͅΣa'.swapcase(), 'aΙσA')
    self.assertEqual('AͅΣ'.swapcase(), 'aΙς')
    self.assertEqual('AΣͅ'.swapcase(), 'aςΙ')
    self.assertEqual('Σͅ '.swapcase(), 'σΙ ')
    self.assertEqual('Σ'.swapcase(), 'σ')
    self.assertEqual('ß'.swapcase(), 'SS')
    self.assertEqual('ῒ'.swapcase(), 'Ϊ̀')
