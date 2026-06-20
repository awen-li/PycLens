# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_decompress_incomplete_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_XZ[:128])
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_ALONE[:128])
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_RAW_1[:128], format=lzma.FORMAT_RAW, filters=FILTERS_RAW_1)
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_RAW_2[:128], format=lzma.FORMAT_RAW, filters=FILTERS_RAW_2)
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_RAW_3[:128], format=lzma.FORMAT_RAW, filters=FILTERS_RAW_3)
    self.assertRaises(LZMAError, lzma.decompress, COMPRESSED_RAW_4[:128], format=lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
