# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_roundtrip_raw_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzc = LZMACompressor(lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    cdata = lzc.compress(INPUT)
    cdata += lzc.compress(b'')
    cdata += lzc.compress(b'')
    cdata += lzc.compress(b'')
    cdata += lzc.flush()
    lzd = LZMADecompressor(lzma.FORMAT_RAW, filters=FILTERS_RAW_4)
    self._test_decompressor(lzd, cdata, lzma.CHECK_NONE)
