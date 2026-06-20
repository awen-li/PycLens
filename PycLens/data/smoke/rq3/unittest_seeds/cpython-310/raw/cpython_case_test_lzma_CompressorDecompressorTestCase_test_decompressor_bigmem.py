# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_decompressor_bigmem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lzd = LZMADecompressor()
    blocksize = 10 * 1024 * 1024
    block = random.randbytes(blocksize)
    try:
        input = block * (size // blocksize + 1)
        cdata = lzma.compress(input)
        ddata = lzd.decompress(cdata)
        self.assertEqual(ddata, input)
    finally:
        input = cdata = ddata = None
