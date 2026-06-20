# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_utf8_decode_valid_sequences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sequences = [(b'\x00', '\x00'), (b'a', 'a'), (b'\x7f', '\x7f'), (b'\xc2\x80', '\x80'), (b'\xdf\xbf', '߿'), (b'\xe0\xa0\x80', 'ࠀ'), (b'\xed\x9f\xbf', '\ud7ff'), (b'\xee\x80\x80', '\ue000'), (b'\xef\xbf\xbf', '\uffff'), (b'\xf0\x90\x80\x80', '𐀀'), (b'\xf4\x8f\xbf\xbf', '\U0010ffff')]
    for (seq, res) in sequences:
        self.assertEqual(seq.decode('utf-8'), res)
