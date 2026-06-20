# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_casefold

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('hello'.casefold(), 'hello')
    self.assertEqual('hELlo'.casefold(), 'hello')
    self.assertEqual('ß'.casefold(), 'ss')
    self.assertEqual('ﬁ'.casefold(), 'fi')
    self.assertEqual('Σ'.casefold(), 'σ')
    self.assertEqual('AͅΣ'.casefold(), 'aισ')
    self.assertEqual('µ'.casefold(), 'μ')
