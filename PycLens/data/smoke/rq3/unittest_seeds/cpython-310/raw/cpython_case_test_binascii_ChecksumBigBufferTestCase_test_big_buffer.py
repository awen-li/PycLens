# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: ChecksumBigBufferTestCase_test_big_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'nyan' * (_1G + 1)
    self.assertEqual(binascii.crc32(data), 1044521549)
