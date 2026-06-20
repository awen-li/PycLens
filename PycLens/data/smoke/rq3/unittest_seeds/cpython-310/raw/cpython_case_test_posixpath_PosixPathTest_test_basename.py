# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_basename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(posixpath.basename('/foo/bar'), 'bar')
    self.assertEqual(posixpath.basename('/'), '')
    self.assertEqual(posixpath.basename('foo'), 'foo')
    self.assertEqual(posixpath.basename('////foo'), 'foo')
    self.assertEqual(posixpath.basename('//foo//bar'), 'bar')
    self.assertEqual(posixpath.basename(b'/foo/bar'), b'bar')
    self.assertEqual(posixpath.basename(b'/'), b'')
    self.assertEqual(posixpath.basename(b'foo'), b'foo')
    self.assertEqual(posixpath.basename(b'////foo'), b'foo')
    self.assertEqual(posixpath.basename(b'//foo//bar'), b'bar')
