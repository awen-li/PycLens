# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressTestCase_test_64bit_compress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'x' * size
    try:
        comp = zlib.compress(data, 0)
        self.assertEqual(zlib.decompress(comp), data)
    finally:
        comp = data = None
