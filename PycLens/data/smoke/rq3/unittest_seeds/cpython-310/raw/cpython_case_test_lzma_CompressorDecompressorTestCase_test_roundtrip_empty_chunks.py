# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_roundtrip_empty_chunks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzc = LZMACompressor()
    cdata = []
    for i in range(0, len(INPUT), 10):
        cdata.append(lzc.compress(INPUT[i:i + 10]))
        cdata.append(lzc.compress(b''))
        cdata.append(lzc.compress(b''))
        cdata.append(lzc.compress(b''))
    cdata.append(lzc.flush())
    cdata = b''.join(cdata)
    lzd = LZMADecompressor()
    self._test_decompressor(lzd, cdata, lzma.CHECK_CRC64)
