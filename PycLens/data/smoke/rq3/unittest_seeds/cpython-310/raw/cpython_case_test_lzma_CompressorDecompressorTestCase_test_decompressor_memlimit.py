# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_memlimit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor(memlimit=1024)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_XZ)
    lzd = LZMADecompressor(lzma.FORMAT_XZ, memlimit=1024)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_XZ)
    lzd = LZMADecompressor(lzma.FORMAT_ALONE, memlimit=1024)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_ALONE)
