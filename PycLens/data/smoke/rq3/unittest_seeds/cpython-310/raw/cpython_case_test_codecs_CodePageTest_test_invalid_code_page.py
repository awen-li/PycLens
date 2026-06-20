# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_invalid_code_page

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, codecs.code_page_encode, -1, 'a')
    self.assertRaises(ValueError, codecs.code_page_decode, -1, b'a')
    self.assertRaises(OSError, codecs.code_page_encode, 123, 'a')
    self.assertRaises(OSError, codecs.code_page_decode, 123, b'a')
