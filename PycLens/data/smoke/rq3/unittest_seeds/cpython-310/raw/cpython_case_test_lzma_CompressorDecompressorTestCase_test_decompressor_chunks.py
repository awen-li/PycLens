# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_chunks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    out = []
    for i in range(0, len(COMPRESSED_XZ), 10):
        self.assertFalse(lzd.eof)
        out.append(lzd.decompress(COMPRESSED_XZ[i:i + 10]))
    out = b''.join(out)
    self.assertEqual(out, INPUT)
    self.assertEqual(lzd.check, lzma.CHECK_CRC64)
    self.assertTrue(lzd.eof)
    self.assertEqual(lzd.unused_data, b'')
