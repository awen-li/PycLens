# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompress_unused_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = b'abcdefghijklmnopqrstuvwxyz'
    remainder = b'0123456789'
    y = zlib.compress(source)
    x = y + remainder
    for maxlen in (0, 1000):
        for step in (1, 2, len(y), len(x)):
            dco = zlib.decompressobj()
            data = b''
            for i in range(0, len(x), step):
                if i < len(y):
                    self.assertEqual(dco.unused_data, b'')
                if maxlen == 0:
                    data += dco.decompress(x[i:i + step])
                    self.assertEqual(dco.unconsumed_tail, b'')
                else:
                    data += dco.decompress(dco.unconsumed_tail + x[i:i + step], maxlen)
            data += dco.flush()
            self.assertTrue(dco.eof)
            self.assertEqual(data, source)
            self.assertEqual(dco.unconsumed_tail, b'')
            self.assertEqual(dco.unused_data, remainder)
