# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_dictionary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = HAMLET_SCENE
    words = h.split()
    random.shuffle(words)
    zdict = b''.join(words)
    co = zlib.compressobj(zdict=zdict)
    cd = co.compress(h) + co.flush()
    dco = zlib.decompressobj(zdict=zdict)
    self.assertEqual(dco.decompress(cd) + dco.flush(), h)
    dco = zlib.decompressobj()
    self.assertRaises(zlib.error, dco.decompress, cd)
