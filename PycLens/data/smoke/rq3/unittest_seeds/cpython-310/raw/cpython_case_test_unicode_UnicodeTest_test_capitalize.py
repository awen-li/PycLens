# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_capitalize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_capitalize(self)
    self.assertEqual('𐑏'.capitalize(), '𐐧')
    self.assertEqual('𐑏𐑏'.capitalize(), '𐐧𐑏')
    self.assertEqual('𐐧𐑏'.capitalize(), '𐐧𐑏')
    self.assertEqual('𐑏𐐧'.capitalize(), '𐐧𐑏')
    self.assertEqual('X𐐧x𐑏'.capitalize(), 'X𐑏x𐑏')
    self.assertEqual('hİ'.capitalize(), 'Hi̇')
    exp = 'Ϊ̀i̇'
    self.assertEqual('ῒİ'.capitalize(), exp)
    self.assertEqual('ﬁnnish'.capitalize(), 'Finnish')
    self.assertEqual('AͅΣ'.capitalize(), 'Aͅς')
