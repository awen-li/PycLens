# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_unused_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    extra = b'fooblibar'
    self._test_decompressor(lzd, COMPRESSED_XZ + extra, lzma.CHECK_CRC64, unused_data=extra)
