# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_compressincremental

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = HAMLET_SCENE * 128
    co = zlib.compressobj()
    bufs = []
    for i in range(0, len(data), 256):
        bufs.append(co.compress(data[i:i + 256]))
    bufs.append(co.flush())
    combuf = b''.join(bufs)
    dco = zlib.decompressobj()
    y1 = dco.decompress(b''.join(bufs))
    y2 = dco.flush()
    self.assertEqual(data, y1 + y2)
