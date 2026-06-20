# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressTestCase_test_speech128

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = HAMLET_SCENE * 128
    x = zlib.compress(data)
    self.assertEqual(zlib.compress(bytearray(data)), x)
    for ob in (x, bytearray(x)):
        self.assertEqual(zlib.decompress(ob), data)
