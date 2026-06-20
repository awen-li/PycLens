# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_escape_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encode = codecs.unicode_escape_encode
    check = coding_checker(self, encode)
    check('\t', b'\\t')
    check('\n', b'\\n')
    check('\r', b'\\r')
    check('\\', b'\\\\')
    for b in range(32):
        if chr(b) not in '\t\n\r':
            check(chr(b), ('\\x%02x' % b).encode())
    for b in range(127, 256):
        check(chr(b), ('\\x%02x' % b).encode())
    check('€', b'\\u20ac')
    check('𝄠', b'\\U0001d120')
