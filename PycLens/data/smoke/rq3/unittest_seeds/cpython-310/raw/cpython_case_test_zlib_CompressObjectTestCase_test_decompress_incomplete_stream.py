# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompress_incomplete_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'x\x9cK\xcb\xcf\x07\x00\x02\x82\x01E'
    self.assertEqual(zlib.decompress(x), b'foo')
    self.assertRaises(zlib.error, zlib.decompress, x[:-5])
    dco = zlib.decompressobj()
    y = dco.decompress(x[:-5])
    y += dco.flush()
    self.assertEqual(y, b'foo')
