# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_inputbuf_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    out = []
    out.append(lzd.decompress(COMPRESSED_XZ[:200], 5))
    out.append(lzd.decompress(COMPRESSED_XZ[200:300], 5))
    out.append(lzd.decompress(COMPRESSED_XZ[300:]))
    self.assertEqual(b''.join(out), INPUT)
