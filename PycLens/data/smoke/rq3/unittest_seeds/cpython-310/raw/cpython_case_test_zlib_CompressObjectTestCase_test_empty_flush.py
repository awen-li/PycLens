# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_empty_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
    self.assertTrue(co.flush())
    dco = zlib.decompressobj()
    self.assertEqual(dco.flush(), b'')
