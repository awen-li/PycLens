# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_maxlen_large

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = HAMLET_SCENE * 10
    self.assertGreater(len(data), zlib.DEF_BUF_SIZE)
    compressed = zlib.compress(data, 1)
    dco = zlib.decompressobj()
    self.assertEqual(dco.decompress(compressed, sys.maxsize), data)
