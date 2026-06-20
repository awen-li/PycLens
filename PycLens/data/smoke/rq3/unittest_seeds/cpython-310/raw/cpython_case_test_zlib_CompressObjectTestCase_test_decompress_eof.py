# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompress_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'x\x9cK\xcb\xcf\x07\x00\x02\x82\x01E'
    dco = zlib.decompressobj()
    self.assertFalse(dco.eof)
    dco.decompress(x[:-5])
    self.assertFalse(dco.eof)
    dco.decompress(x[-5:])
    self.assertTrue(dco.eof)
    dco.flush()
    self.assertTrue(dco.eof)
