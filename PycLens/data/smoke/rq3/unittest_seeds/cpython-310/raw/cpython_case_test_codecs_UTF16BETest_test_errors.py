# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF16BETest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'\xff', '�'), (b'\x00A\xff', 'A�'), (b'\x00A\x00B\x00C\x00DZ', 'ABCD�'), (b'\xd8\x00', '�'), (b'\xd8\x00\xdc', '�'), (b'\xd8\x00\x00A', '�A'), (b'\xdc\x00\x00A', '�A')]
    for (raw, expected) in tests:
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_be_decode, raw, 'strict', True)
        self.assertEqual(raw.decode('utf-16be', 'replace'), expected)
