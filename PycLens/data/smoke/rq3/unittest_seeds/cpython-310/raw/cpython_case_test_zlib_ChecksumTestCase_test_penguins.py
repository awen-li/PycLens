# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_penguins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(zlib.crc32(b'penguin', 0), 3854672160)
    self.assertEqual(zlib.crc32(b'penguin', 1), 1136044692)
    self.assertEqual(zlib.adler32(b'penguin', 0), 198116086)
    self.assertEqual(zlib.adler32(b'penguin', 1), 198574839)
    self.assertEqual(zlib.crc32(b'penguin'), zlib.crc32(b'penguin', 0))
    self.assertEqual(zlib.adler32(b'penguin'), zlib.adler32(b'penguin', 1))
