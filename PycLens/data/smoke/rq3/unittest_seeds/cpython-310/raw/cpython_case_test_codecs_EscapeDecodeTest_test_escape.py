# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EscapeDecodeTest_test_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.escape_decode
    check = coding_checker(self, decode)
    check(b'[\\\n]', b'[]')
    check(b'[\\"]', b'["]')
    check(b"[\\']", b"[']")
    check(b'[\\\\]', b'[\\]')
    check(b'[\\a]', b'[\x07]')
    check(b'[\\b]', b'[\x08]')
    check(b'[\\t]', b'[\t]')
    check(b'[\\n]', b'[\n]')
    check(b'[\\v]', b'[\x0b]')
    check(b'[\\f]', b'[\x0c]')
    check(b'[\\r]', b'[\r]')
    check(b'[\\7]', b'[\x07]')
    check(b'[\\78]', b'[\x078]')
    check(b'[\\41]', b'[!]')
    check(b'[\\418]', b'[!8]')
    check(b'[\\101]', b'[A]')
    check(b'[\\1010]', b'[A0]')
    check(b'[\\501]', b'[A]')
    check(b'[\\x41]', b'[A]')
    check(b'[\\x410]', b'[A0]')
    for i in range(97, 123):
        b = bytes([i])
        if b not in b'abfnrtvx':
            with self.assertWarns(DeprecationWarning):
                check(b'\\' + b, b'\\' + b)
        with self.assertWarns(DeprecationWarning):
            check(b'\\' + b.upper(), b'\\' + b.upper())
    with self.assertWarns(DeprecationWarning):
        check(b'\\8', b'\\8')
    with self.assertWarns(DeprecationWarning):
        check(b'\\9', b'\\9')
    with self.assertWarns(DeprecationWarning):
        check(b'\\\xfa', b'\\\xfa')
