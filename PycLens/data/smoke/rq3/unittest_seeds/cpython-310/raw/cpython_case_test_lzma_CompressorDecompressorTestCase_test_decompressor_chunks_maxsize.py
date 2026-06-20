# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_chunks_maxsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    max_length = 100
    out = []
    len_ = len(COMPRESSED_XZ) // 2
    out.append(lzd.decompress(COMPRESSED_XZ[:len_], max_length=max_length))
    self.assertFalse(lzd.needs_input)
    self.assertEqual(len(out[-1]), max_length)
    out.append(lzd.decompress(b'', max_length=max_length))
    self.assertFalse(lzd.needs_input)
    self.assertEqual(len(out[-1]), max_length)
    out.append(lzd.decompress(COMPRESSED_XZ[len_:], max_length=max_length))
    self.assertLessEqual(len(out[-1]), max_length)
    while not lzd.eof:
        out.append(lzd.decompress(b'', max_length=max_length))
        self.assertLessEqual(len(out[-1]), max_length)
    out = b''.join(out)
    self.assertEqual(out, INPUT)
    self.assertEqual(lzd.check, lzma.CHECK_CRC64)
    self.assertEqual(lzd.unused_data, b'')
