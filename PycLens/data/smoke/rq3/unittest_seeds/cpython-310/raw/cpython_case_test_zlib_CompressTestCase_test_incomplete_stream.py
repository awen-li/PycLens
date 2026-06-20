# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressTestCase_test_incomplete_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = zlib.compress(HAMLET_SCENE)
    self.assertRaisesRegex(zlib.error, 'Error -5 while decompressing data: incomplete or truncated stream', zlib.decompress, x[:-1])
