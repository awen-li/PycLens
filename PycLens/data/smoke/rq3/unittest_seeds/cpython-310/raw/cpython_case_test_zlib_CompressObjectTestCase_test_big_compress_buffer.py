# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_big_compress_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = zlib.compressobj(1)
    compress = lambda s: c.compress(s) + c.flush()
    self.check_big_compress_buffer(size, compress)
