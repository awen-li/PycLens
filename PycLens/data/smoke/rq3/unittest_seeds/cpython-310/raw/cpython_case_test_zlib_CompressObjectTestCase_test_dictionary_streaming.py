# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_dictionary_streaming

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co = zlib.compressobj(zdict=HAMLET_SCENE)
    do = zlib.decompressobj(zdict=HAMLET_SCENE)
    piece = HAMLET_SCENE[1000:1500]
    d0 = co.compress(piece) + co.flush(zlib.Z_SYNC_FLUSH)
    d1 = co.compress(piece[100:]) + co.flush(zlib.Z_SYNC_FLUSH)
    d2 = co.compress(piece[:-100]) + co.flush(zlib.Z_SYNC_FLUSH)
    self.assertEqual(do.decompress(d0), piece)
    self.assertEqual(do.decompress(d1), piece[100:])
    self.assertEqual(do.decompress(d2), piece[:-100])
