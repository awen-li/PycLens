# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF16LETest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'\xff', '�'), (b'A\x00Z', 'A�'), (b'A\x00B\x00C\x00D\x00Z', 'ABCD�'), (b'\x00\xd8', '�'), (b'\x00\xd8A', '�'), (b'\x00\xd8A\x00', '�A'), (b'\x00\xdcA\x00', '�A')]
    for (raw, expected) in tests:
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_le_decode, raw, 'strict', True)
        self.assertEqual(raw.decode('utf-16le', 'replace'), expected)
