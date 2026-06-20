# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompimax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = source or HAMLET_SCENE
    data = source * 128
    co = zlib.compressobj()
    bufs = []
    for i in range(0, len(data), cx):
        bufs.append(co.compress(data[i:i + cx]))
    bufs.append(co.flush())
    combuf = b''.join(bufs)
    self.assertEqual(data, zlib.decompress(combuf), 'compressed data failure')
    dco = zlib.decompressobj()
    bufs = []
    cb = combuf
    while cb:
        chunk = dco.decompress(cb, dcx)
        self.assertFalse(len(chunk) > dcx, 'chunk too big (%d>%d)' % (len(chunk), dcx))
        bufs.append(chunk)
        cb = dco.unconsumed_tail
    bufs.append(dco.flush())
    self.assertEqual(data, b''.join(bufs), 'Wrong data retrieved')
