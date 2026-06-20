# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_large_unconsumed_tail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'x' * size
    do = zlib.decompressobj()
    try:
        comp = zlib.compress(data, 0)
        uncomp = do.decompress(comp, 1) + do.flush()
        self.assertEqual(uncomp, data)
        self.assertEqual(do.unconsumed_tail, b'')
    finally:
        comp = uncomp = data = None
