# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_64bit_compress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'x' * size
    co = zlib.compressobj(0)
    do = zlib.decompressobj()
    try:
        comp = co.compress(data) + co.flush()
        uncomp = do.decompress(comp) + do.flush()
        self.assertEqual(uncomp, data)
    finally:
        comp = uncomp = data = None
