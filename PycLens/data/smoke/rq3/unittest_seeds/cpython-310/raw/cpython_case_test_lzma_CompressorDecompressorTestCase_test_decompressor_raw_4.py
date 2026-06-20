# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_raw_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor(lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    self._test_decompressor(lzd, COMPRESSED_RAW_4, lzma.CHECK_NONE)
