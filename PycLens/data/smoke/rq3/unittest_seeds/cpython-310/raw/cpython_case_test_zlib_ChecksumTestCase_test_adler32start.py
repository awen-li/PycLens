# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_adler32start

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(zlib.adler32(b''), zlib.adler32(b'', 1))
    self.assertTrue(zlib.adler32(b'abc', 4294967295))
