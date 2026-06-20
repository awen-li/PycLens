# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ExceptionTestCase_test_badargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, zlib.adler32)
    self.assertRaises(TypeError, zlib.crc32)
    self.assertRaises(TypeError, zlib.compress)
    self.assertRaises(TypeError, zlib.decompress)
    for arg in (42, None, '', 'abc', (), []):
        self.assertRaises(TypeError, zlib.adler32, arg)
        self.assertRaises(TypeError, zlib.crc32, arg)
        self.assertRaises(TypeError, zlib.compress, arg)
        self.assertRaises(TypeError, zlib.decompress, arg)
