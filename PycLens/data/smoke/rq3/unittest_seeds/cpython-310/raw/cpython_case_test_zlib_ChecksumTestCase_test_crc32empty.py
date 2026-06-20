# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_crc32empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(zlib.crc32(b'', 0), 0)
    self.assertEqual(zlib.crc32(b'', 1), 1)
    self.assertEqual(zlib.crc32(b'', 432), 432)
