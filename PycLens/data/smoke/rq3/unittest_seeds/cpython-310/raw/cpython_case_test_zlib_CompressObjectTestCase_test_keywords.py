# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    level = 2
    method = zlib.DEFLATED
    wbits = -12
    memLevel = 9
    strategy = zlib.Z_FILTERED
    co = zlib.compressobj(level=level, method=method, wbits=wbits, memLevel=memLevel, strategy=strategy, zdict=b'')
    do = zlib.decompressobj(wbits=wbits, zdict=b'')
    with self.assertRaises(TypeError):
        co.compress(data=HAMLET_SCENE)
    with self.assertRaises(TypeError):
        do.decompress(data=zlib.compress(HAMLET_SCENE))
    x = co.compress(HAMLET_SCENE) + co.flush()
    y = do.decompress(x, max_length=len(HAMLET_SCENE)) + do.flush()
    self.assertEqual(HAMLET_SCENE, y)
