# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_large_utf8_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = b'0123456\xed\x84\x80' * (size // 8)
    self.assertEqual(len(encoded), size // 8 * 10)
    decoded = codecs.code_page_decode(65001, encoded, 'ignore', True)
    self.assertEqual(decoded[1], len(encoded))
    del encoded
    self.assertEqual(len(decoded[0]), size)
    self.assertEqual(decoded[0][:10], '0123456턀01')
    self.assertEqual(decoded[0][-11:], '56턀0123456턀')
