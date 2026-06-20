# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_inputbuf_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    out = []
    self.assertEqual(lzd.decompress(COMPRESSED_XZ[:200], max_length=0), b'')
    out.append(lzd.decompress(b''))
    out.append(lzd.decompress(COMPRESSED_XZ[200:280], 2))
    out.append(lzd.decompress(COMPRESSED_XZ[280:300], 2))
    out.append(lzd.decompress(COMPRESSED_XZ[300:]))
    self.assertEqual(b''.join(out), INPUT)
