# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_flush_large_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = HAMLET_SCENE * 10
    data = zlib.compress(input, 1)
    dco = zlib.decompressobj()
    dco.decompress(data, 1)
    self.assertEqual(dco.flush(size), input[1:])
