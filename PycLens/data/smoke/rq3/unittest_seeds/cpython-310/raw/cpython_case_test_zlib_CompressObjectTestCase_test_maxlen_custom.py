# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_maxlen_custom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = HAMLET_SCENE * 10
    compressed = zlib.compress(data, 1)
    dco = zlib.decompressobj()
    self.assertEqual(dco.decompress(compressed, CustomInt()), data[:100])
