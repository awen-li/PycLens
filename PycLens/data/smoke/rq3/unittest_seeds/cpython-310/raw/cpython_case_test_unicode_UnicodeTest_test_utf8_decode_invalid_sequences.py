# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_utf8_decode_invalid_sequences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    continuation_bytes = [bytes([x]) for x in range(128, 192)]
    invalid_2B_seq_start_bytes = [bytes([x]) for x in range(192, 194)]
    invalid_4B_seq_start_bytes = [bytes([x]) for x in range(245, 248)]
    invalid_start_bytes = continuation_bytes + invalid_2B_seq_start_bytes + invalid_4B_seq_start_bytes + [bytes([x]) for x in range(247, 256)]
    for byte in invalid_start_bytes:
        self.assertRaises(UnicodeDecodeError, byte.decode, 'utf-8')
    for sb in invalid_2B_seq_start_bytes:
        for cb in continuation_bytes:
            self.assertRaises(UnicodeDecodeError, (sb + cb).decode, 'utf-8')
    for sb in invalid_4B_seq_start_bytes:
        for cb1 in continuation_bytes[:3]:
            for cb3 in continuation_bytes[:3]:
                self.assertRaises(UnicodeDecodeError, (sb + cb1 + b'\x80' + cb3).decode, 'utf-8')
    for cb in [bytes([x]) for x in range(128, 160)]:
        self.assertRaises(UnicodeDecodeError, (b'\xe0' + cb + b'\x80').decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, (b'\xe0' + cb + b'\xbf').decode, 'utf-8')
    for cb in [bytes([x]) for x in range(160, 192)]:
        self.assertRaises(UnicodeDecodeError, (b'\xed' + cb + b'\x80').decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, (b'\xed' + cb + b'\xbf').decode, 'utf-8')
    for cb in [bytes([x]) for x in range(128, 144)]:
        self.assertRaises(UnicodeDecodeError, (b'\xf0' + cb + b'\x80\x80').decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, (b'\xf0' + cb + b'\xbf\xbf').decode, 'utf-8')
    for cb in [bytes([x]) for x in range(144, 192)]:
        self.assertRaises(UnicodeDecodeError, (b'\xf4' + cb + b'\x80\x80').decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, (b'\xf4' + cb + b'\xbf\xbf').decode, 'utf-8')
