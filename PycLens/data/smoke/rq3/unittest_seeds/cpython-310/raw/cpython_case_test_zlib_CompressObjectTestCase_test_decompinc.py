# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompinc

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
    decombuf = zlib.decompress(combuf)
    self.assertIsInstance(decombuf, bytes)
    self.assertEqual(data, decombuf)
    dco = zlib.decompressobj()
    bufs = []
    for i in range(0, len(combuf), dcx):
        bufs.append(dco.decompress(combuf[i:i + dcx]))
        self.assertEqual(b'', dco.unconsumed_tail, "(A) uct should be b'': not %d long" % len(dco.unconsumed_tail))
        self.assertEqual(b'', dco.unused_data)
    if flush:
        bufs.append(dco.flush())
    else:
        while True:
            chunk = dco.decompress(b'')
            if chunk:
                bufs.append(chunk)
            else:
                break
    self.assertEqual(b'', dco.unconsumed_tail, "(B) uct should be b'': not %d long" % len(dco.unconsumed_tail))
    self.assertEqual(b'', dco.unused_data)
    self.assertEqual(data, b''.join(bufs))
