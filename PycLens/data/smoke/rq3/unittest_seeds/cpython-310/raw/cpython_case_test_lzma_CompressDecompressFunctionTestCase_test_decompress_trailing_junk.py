# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_decompress_trailing_junk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ddata = lzma.decompress(COMPRESSED_XZ + COMPRESSED_BOGUS)
    self.assertEqual(ddata, INPUT)
