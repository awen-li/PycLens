# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressTestCase_test_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = zlib.compress(HAMLET_SCENE, level=3)
    self.assertEqual(zlib.decompress(x), HAMLET_SCENE)
    with self.assertRaises(TypeError):
        zlib.compress(data=HAMLET_SCENE, level=3)
    self.assertEqual(zlib.decompress(x, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE), HAMLET_SCENE)
