# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_escape_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.unicode_escape_decode
    check = coding_checker(self, decode)
    check(b'[\\\n]', '[]')
    check(b'[\\"]', '["]')
    check(b"[\\']", "[']")
    check(b'[\\\\]', '[\\]')
    check(b'[\\a]', '[\x07]')
    check(b'[\\b]', '[\x08]')
    check(b'[\\t]', '[\t]')
    check(b'[\\n]', '[\n]')
    check(b'[\\v]', '[\x0b]')
    check(b'[\\f]', '[\x0c]')
    check(b'[\\r]', '[\r]')
    check(b'[\\7]', '[\x07]')
    check(b'[\\78]', '[\x078]')
    check(b'[\\41]', '[!]')
    check(b'[\\418]', '[!8]')
    check(b'[\\101]', '[A]')
    check(b'[\\1010]', '[A0]')
    check(b'[\\x41]', '[A]')
    check(b'[\\x410]', '[A0]')
    check(b'\\u20ac', '€')
    check(b'\\U0001d120', '𝄠')
    for i in range(97, 123):
        b = bytes([i])
        if b not in b'abfnrtuvx':
            with self.assertWarns(DeprecationWarning):
                check(b'\\' + b, '\\' + chr(i))
        if b.upper() not in b'UN':
            with self.assertWarns(DeprecationWarning):
                check(b'\\' + b.upper(), '\\' + chr(i - 32))
    with self.assertWarns(DeprecationWarning):
        check(b'\\8', '\\8')
    with self.assertWarns(DeprecationWarning):
        check(b'\\9', '\\9')
    with self.assertWarns(DeprecationWarning):
        check(b'\\\xfa', '\\ú')
