# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompresscopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = HAMLET_SCENE
    comp = zlib.compress(data)
    self.assertIsInstance(comp, bytes)
    for func in (lambda c: c.copy(), copy.copy, copy.deepcopy):
        d0 = zlib.decompressobj()
        bufs0 = []
        bufs0.append(d0.decompress(comp[:32]))
        d1 = func(d0)
        bufs1 = bufs0[:]
        bufs0.append(d0.decompress(comp[32:]))
        s0 = b''.join(bufs0)
        bufs1.append(d1.decompress(comp[32:]))
        s1 = b''.join(bufs1)
        self.assertEqual(s0, s1)
        self.assertEqual(s0, data)
