# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_decode_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.unicode_escape_decode
    for (c, d) in ((b'x', 2), (b'u', 4), (b'U', 4)):
        for i in range(d):
            self.assertRaises(UnicodeDecodeError, decode, b'\\' + c + b'0' * i)
            self.assertRaises(UnicodeDecodeError, decode, b'[\\' + c + b'0' * i + b']')
            data = b'[\\' + c + b'0' * i + b']\\' + c + b'0' * i
            self.assertEqual(decode(data, 'ignore'), ('[]', len(data)))
            self.assertEqual(decode(data, 'replace'), ('[�]�', len(data)))
    self.assertRaises(UnicodeDecodeError, decode, b'\\U00110000')
    self.assertEqual(decode(b'\\U00110000', 'ignore'), ('', 10))
    self.assertEqual(decode(b'\\U00110000', 'replace'), ('�', 10))
