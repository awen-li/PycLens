# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_big_decompress_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = zlib.decompressobj()
    decompress = lambda s: d.decompress(s) + d.flush()
    self.check_big_decompress_buffer(size, decompress)
