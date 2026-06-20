# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_bad_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_RAW_1)
    lzd = LZMADecompressor(lzma.FORMAT_XZ)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_ALONE)
    lzd = LZMADecompressor(lzma.FORMAT_ALONE)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_XZ)
    lzd = LZMADecompressor(lzma.FORMAT_RAW, filters=FILTERS_RAW_1)
    self.assertRaises(LZMAError, lzd.decompress, COMPRESSED_XZ)
