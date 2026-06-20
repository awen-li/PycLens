# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_invalid_start_byte

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FFFD = '�'
    for byte in b'\x80\xa0\x9f\xbf\xc0\xc1\xf5\xff':
        self.assertCorrectUTF8Decoding(bytes([byte]), '�', 'invalid start byte')
