# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_decompress_bad_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_BOGUS)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_RAW_1)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_ALONE, format=lzma.FORMAT_XZ)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, format=lzma.FORMAT_ALONE)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, format=lzma.FORMAT_RAW, filters=FILTERS_RAW_1)
