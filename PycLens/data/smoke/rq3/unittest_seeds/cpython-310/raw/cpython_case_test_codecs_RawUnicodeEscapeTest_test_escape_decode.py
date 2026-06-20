# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: RawUnicodeEscapeTest_test_escape_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.raw_unicode_escape_decode
    check = coding_checker(self, decode)
    for b in range(256):
        if b not in b'uU':
            check(b'\\' + bytes([b]), '\\' + chr(b))
    check(b'\\u20ac', '€')
    check(b'\\U0001d120', '𝄠')
