# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_builtin_decode_length_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(UnicodeError, 'too long'):
        (b'xn--016c' + b'a' * 1100).decode('idna')
    with self.assertRaisesRegex(UnicodeError, 'too long'):
        (b'xn--016c' + b'a' * 70).decode('idna')
