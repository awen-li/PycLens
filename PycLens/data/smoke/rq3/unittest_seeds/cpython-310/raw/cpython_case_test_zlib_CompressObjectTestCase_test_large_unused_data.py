# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_large_unused_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'abcdefghijklmnop'
    unused = b'x' * size
    comp = zlib.compress(data) + unused
    do = zlib.decompressobj()
    try:
        uncomp = do.decompress(comp) + do.flush()
        self.assertEqual(unused, do.unused_data)
        self.assertEqual(uncomp, data)
    finally:
        unused = comp = do = None
