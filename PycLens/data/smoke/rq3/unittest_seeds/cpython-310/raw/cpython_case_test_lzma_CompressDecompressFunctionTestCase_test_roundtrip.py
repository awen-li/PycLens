# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cdata = lzma.compress(INPUT)
    ddata = lzma.decompress(cdata)
    self.assertEqual(ddata, INPUT)
    cdata = lzma.compress(INPUT, lzma.FORMAT_XZ)
    ddata = lzma.decompress(cdata)
    self.assertEqual(ddata, INPUT)
    cdata = lzma.compress(INPUT, lzma.FORMAT_ALONE)
    ddata = lzma.decompress(cdata)
    self.assertEqual(ddata, INPUT)
    cdata = lzma.compress(INPUT, lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    ddata = lzma.decompress(cdata, lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    self.assertEqual(ddata, INPUT)
