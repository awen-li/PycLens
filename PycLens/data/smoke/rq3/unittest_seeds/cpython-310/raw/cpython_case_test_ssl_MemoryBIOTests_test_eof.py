# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: MemoryBIOTests_test_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = ssl.MemoryBIO()
    self.assertFalse(bio.eof)
    self.assertEqual(bio.read(), b'')
    self.assertFalse(bio.eof)
    bio.write(b'foo')
    self.assertFalse(bio.eof)
    bio.write_eof()
    self.assertFalse(bio.eof)
    self.assertEqual(bio.read(2), b'fo')
    self.assertFalse(bio.eof)
    self.assertEqual(bio.read(1), b'o')
    self.assertTrue(bio.eof)
    self.assertEqual(bio.read(), b'')
    self.assertTrue(bio.eof)
