# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompressmaxlen

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
    self.assertEqual(data, zlib.decompress(combuf), 'compressed data failure')
    dco = zlib.decompressobj()
    bufs = []
    cb = combuf
    while cb:
        max_length = 1 + len(cb) // 10
        chunk = dco.decompress(cb, max_length)
        self.assertFalse(len(chunk) > max_length, 'chunk too big (%d>%d)' % (len(chunk), max_length))
        bufs.append(chunk)
        cb = dco.unconsumed_tail
    if flush:
        bufs.append(dco.flush())
    else:
        while chunk:
            chunk = dco.decompress(b'', max_length)
            self.assertFalse(len(chunk) > max_length, 'chunk too big (%d>%d)' % (len(chunk), max_length))
            bufs.append(chunk)
    self.assertEqual(data, b''.join(bufs), 'Wrong data retrieved')
