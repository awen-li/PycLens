# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_compresscopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data0 = HAMLET_SCENE
    data1 = bytes(str(HAMLET_SCENE, 'ascii').swapcase(), 'ascii')
    for func in (lambda c: c.copy(), copy.copy, copy.deepcopy):
        c0 = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
        bufs0 = []
        bufs0.append(c0.compress(data0))
        c1 = func(c0)
        bufs1 = bufs0[:]
        bufs0.append(c0.compress(data0))
        bufs0.append(c0.flush())
        s0 = b''.join(bufs0)
        bufs1.append(c1.compress(data1))
        bufs1.append(c1.flush())
        s1 = b''.join(bufs1)
        self.assertEqual(zlib.decompress(s0), data0 + data0)
        self.assertEqual(zlib.decompress(s1), data0 + data1)
