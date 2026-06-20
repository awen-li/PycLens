# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_bad_filter_spec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, LZMACompressor, filters=[b'wobsite'])
    self.assertRaises(ValueError, LZMACompressor, filters=[{'xyzzy': 3}])
    self.assertRaises(ValueError, LZMACompressor, filters=[{'id': 98765}])
    with self.assertRaises(ValueError):
        LZMACompressor(filters=[{'id': lzma.FILTER_LZMA2, 'foo': 0}])
    with self.assertRaises(ValueError):
        LZMACompressor(filters=[{'id': lzma.FILTER_DELTA, 'foo': 0}])
    with self.assertRaises(ValueError):
        LZMACompressor(filters=[{'id': lzma.FILTER_X86, 'foo': 0}])
