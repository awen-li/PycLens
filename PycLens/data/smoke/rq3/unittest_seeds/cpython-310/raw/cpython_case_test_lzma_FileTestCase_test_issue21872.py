# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_issue21872

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = LZMADecompressor()
    entire = d1.decompress(ISSUE_21872_DAT, max_length=-1)
    self.assertEqual(len(entire), 13160)
    self.assertTrue(d1.eof)
    d2 = LZMADecompressor()
    out1 = d2.decompress(ISSUE_21872_DAT, max_length=13149)
    self.assertFalse(d2.needs_input)
    self.assertFalse(d2.eof)
    out2 = d2.decompress(b'')
    self.assertEqual(len(out2), 11)
    self.assertTrue(d2.eof)
    self.assertEqual(out1 + out2, entire)
