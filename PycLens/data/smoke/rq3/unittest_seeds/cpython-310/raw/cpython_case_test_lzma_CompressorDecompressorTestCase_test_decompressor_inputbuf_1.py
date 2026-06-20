# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_inputbuf_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    out = []
    self.assertEqual(lzd.decompress(COMPRESSED_XZ[:100], max_length=0), b'')
    out.append(lzd.decompress(b'', 2))
    out.append(lzd.decompress(COMPRESSED_XZ[100:105], 15))
    out.append(lzd.decompress(COMPRESSED_XZ[105:]))
    self.assertEqual(b''.join(out), INPUT)
