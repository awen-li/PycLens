# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_pair

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    datasrc = HAMLET_SCENE * 128
    datazip = zlib.compress(datasrc)
    for data in (datasrc, bytearray(datasrc)):
        co = zlib.compressobj()
        x1 = co.compress(data)
        x2 = co.flush()
        self.assertRaises(zlib.error, co.flush)
        self.assertEqual(x1 + x2, datazip)
    for (v1, v2) in ((x1, x2), (bytearray(x1), bytearray(x2))):
        dco = zlib.decompressobj()
        y1 = dco.decompress(v1 + v2)
        y2 = dco.flush()
        self.assertEqual(data, y1 + y2)
        self.assertIsInstance(dco.unconsumed_tail, bytes)
        self.assertIsInstance(dco.unused_data, bytes)
