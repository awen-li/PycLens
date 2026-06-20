# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_code_page_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaisesRegex(UnicodeEncodeError, 'cp932', codecs.code_page_encode, 932, 'ÿ')
    self.assertRaisesRegex(UnicodeDecodeError, 'cp932', codecs.code_page_decode, 932, b'\x81\x00', 'strict', True)
    self.assertRaisesRegex(UnicodeDecodeError, 'CP_UTF8', codecs.code_page_decode, self.CP_UTF8, b'\xff', 'strict', True)
