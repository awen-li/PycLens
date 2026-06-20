# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_roundtrip_alone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzc = LZMACompressor(lzma.FORMAT_ALONE)
    cdata = lzc.compress(INPUT) + lzc.flush()
    lzd = LZMADecompressor()
    self._test_decompressor(lzd, cdata, lzma.CHECK_NONE)
