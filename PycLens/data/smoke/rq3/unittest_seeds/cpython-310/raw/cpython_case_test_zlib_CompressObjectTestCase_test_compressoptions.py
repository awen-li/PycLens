# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_compressoptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    level = 2
    method = zlib.DEFLATED
    wbits = -12
    memLevel = 9
    strategy = zlib.Z_FILTERED
    co = zlib.compressobj(level, method, wbits, memLevel, strategy)
    x1 = co.compress(HAMLET_SCENE)
    x2 = co.flush()
    dco = zlib.decompressobj(wbits)
    y1 = dco.decompress(x1 + x2)
    y2 = dco.flush()
    self.assertEqual(HAMLET_SCENE, y1 + y2)
