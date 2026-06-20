# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_decompress_good_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ddata = lzma.decompress(COMPRESSED_XZ)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_ALONE)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_XZ, lzma.FORMAT_XZ)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_ALONE, lzma.FORMAT_ALONE)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_RAW_1, lzma.FORMAT_RAW, filters=FILTERS_RAW_1)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_RAW_2, lzma.FORMAT_RAW, filters=FILTERS_RAW_2)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_RAW_3, lzma.FORMAT_RAW, filters=FILTERS_RAW_3)
    self.assertEqual(ddata, INPUT)
    ddata = lzma.decompress(COMPRESSED_RAW_4, lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    self.assertEqual(ddata, INPUT)
