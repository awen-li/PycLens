# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_isidentifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue('a'.isidentifier())
    self.assertTrue('Z'.isidentifier())
    self.assertTrue('_'.isidentifier())
    self.assertTrue('b0'.isidentifier())
    self.assertTrue('bc'.isidentifier())
    self.assertTrue('b_'.isidentifier())
    self.assertTrue('µ'.isidentifier())
    self.assertTrue('𝔘𝔫𝔦𝔠𝔬𝔡𝔢'.isidentifier())
    self.assertFalse(' '.isidentifier())
    self.assertFalse('['.isidentifier())
    self.assertFalse('©'.isidentifier())
    self.assertFalse('0'.isidentifier())
