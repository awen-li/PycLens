# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: MemoryBIOTests_test_read_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = ssl.MemoryBIO()
    bio.write(b'foo')
    self.assertEqual(bio.read(), b'foo')
    self.assertEqual(bio.read(), b'')
    bio.write(b'foo')
    bio.write(b'bar')
    self.assertEqual(bio.read(), b'foobar')
    self.assertEqual(bio.read(), b'')
    bio.write(b'baz')
    self.assertEqual(bio.read(2), b'ba')
    self.assertEqual(bio.read(1), b'z')
    self.assertEqual(bio.read(1), b'')
