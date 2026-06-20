# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_compressor_bigmem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzc = LZMACompressor()
    cdata = lzc.compress(b'x' * size) + lzc.flush()
    ddata = lzma.decompress(cdata)
    try:
        self.assertEqual(len(ddata), size)
        self.assertEqual(len(ddata.strip(b'x')), 0)
    finally:
        ddata = None
