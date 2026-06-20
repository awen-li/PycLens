# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_crc32start

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(zlib.crc32(b''), zlib.crc32(b'', 0))
    self.assertTrue(zlib.crc32(b'abc', 4294967295))
