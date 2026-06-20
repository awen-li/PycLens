# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_lower

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_lower(self)
    self.assertEqual('𐐧'.lower(), '𐑏')
    self.assertEqual('𐐧𐐧'.lower(), '𐑏𐑏')
    self.assertEqual('𐐧𐑏'.lower(), '𐑏𐑏')
    self.assertEqual('X𐐧x𐑏'.lower(), 'x𐑏x𐑏')
    self.assertEqual('ﬁ'.lower(), 'ﬁ')
    self.assertEqual('İ'.lower(), 'i̇')
    self.assertEqual('Σ'.lower(), 'σ')
    self.assertEqual('ͅΣ'.lower(), 'ͅσ')
    self.assertEqual('AͅΣ'.lower(), 'aͅς')
    self.assertEqual('AͅΣa'.lower(), 'aͅσa')
    self.assertEqual('AͅΣ'.lower(), 'aͅς')
    self.assertEqual('AΣͅ'.lower(), 'aςͅ')
    self.assertEqual('Σͅ '.lower(), 'σͅ ')
    self.assertEqual('\U0008fffe'.lower(), '\U0008fffe')
    self.assertEqual('ⅷ'.lower(), 'ⅷ')
