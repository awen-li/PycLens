# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_wbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v = zlib.ZLIB_RUNTIME_VERSION.split('-', 1)[0].split('.')
    if len(v) < 4:
        v.append('0')
    elif not v[-1].isnumeric():
        v[-1] = '0'
    v = tuple(map(int, v))
    supports_wbits_0 = v >= (1, 2, 3, 5)
    co = zlib.compressobj(level=1, wbits=15)
    zlib15 = co.compress(HAMLET_SCENE) + co.flush()
    self.assertEqual(zlib.decompress(zlib15, 15), HAMLET_SCENE)
    if supports_wbits_0:
        self.assertEqual(zlib.decompress(zlib15, 0), HAMLET_SCENE)
    self.assertEqual(zlib.decompress(zlib15, 32 + 15), HAMLET_SCENE)
    with self.assertRaisesRegex(zlib.error, 'invalid window size'):
        zlib.decompress(zlib15, 14)
    dco = zlib.decompressobj(wbits=32 + 15)
    self.assertEqual(dco.decompress(zlib15), HAMLET_SCENE)
    dco = zlib.decompressobj(wbits=14)
    with self.assertRaisesRegex(zlib.error, 'invalid window size'):
        dco.decompress(zlib15)
    co = zlib.compressobj(level=1, wbits=9)
    zlib9 = co.compress(HAMLET_SCENE) + co.flush()
    self.assertEqual(zlib.decompress(zlib9, 9), HAMLET_SCENE)
    self.assertEqual(zlib.decompress(zlib9, 15), HAMLET_SCENE)
    if supports_wbits_0:
        self.assertEqual(zlib.decompress(zlib9, 0), HAMLET_SCENE)
    self.assertEqual(zlib.decompress(zlib9, 32 + 9), HAMLET_SCENE)
    dco = zlib.decompressobj(wbits=32 + 9)
    self.assertEqual(dco.decompress(zlib9), HAMLET_SCENE)
    co = zlib.compressobj(level=1, wbits=-15)
    deflate15 = co.compress(HAMLET_SCENE) + co.flush()
    self.assertEqual(zlib.decompress(deflate15, -15), HAMLET_SCENE)
    dco = zlib.decompressobj(wbits=-15)
    self.assertEqual(dco.decompress(deflate15), HAMLET_SCENE)
    co = zlib.compressobj(level=1, wbits=-9)
    deflate9 = co.compress(HAMLET_SCENE) + co.flush()
    self.assertEqual(zlib.decompress(deflate9, -9), HAMLET_SCENE)
    self.assertEqual(zlib.decompress(deflate9, -15), HAMLET_SCENE)
    dco = zlib.decompressobj(wbits=-9)
    self.assertEqual(dco.decompress(deflate9), HAMLET_SCENE)
    co = zlib.compressobj(level=1, wbits=16 + 15)
    gzip = co.compress(HAMLET_SCENE) + co.flush()
    self.assertEqual(zlib.decompress(gzip, 16 + 15), HAMLET_SCENE)
    self.assertEqual(zlib.decompress(gzip, 32 + 15), HAMLET_SCENE)
    dco = zlib.decompressobj(32 + 15)
    self.assertEqual(dco.decompress(gzip), HAMLET_SCENE)
