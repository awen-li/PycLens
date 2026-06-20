# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_decompress_memlimit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, memlimit=1024)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, format=lzma.FORMAT_XZ, memlimit=1024)
    with self.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_ALONE, format=lzma.FORMAT_ALONE, memlimit=1024)
