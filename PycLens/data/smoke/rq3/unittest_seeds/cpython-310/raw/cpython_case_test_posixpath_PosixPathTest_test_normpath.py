# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_normpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(posixpath.normpath(''), '.')
    self.assertEqual(posixpath.normpath('/'), '/')
    self.assertEqual(posixpath.normpath('//'), '//')
    self.assertEqual(posixpath.normpath('///'), '/')
    self.assertEqual(posixpath.normpath('///foo/.//bar//'), '/foo/bar')
    self.assertEqual(posixpath.normpath('///foo/.//bar//.//..//.//baz'), '/foo/baz')
    self.assertEqual(posixpath.normpath('///..//./foo/.//bar'), '/foo/bar')
    self.assertEqual(posixpath.normpath(b''), b'.')
    self.assertEqual(posixpath.normpath(b'/'), b'/')
    self.assertEqual(posixpath.normpath(b'//'), b'//')
    self.assertEqual(posixpath.normpath(b'///'), b'/')
    self.assertEqual(posixpath.normpath(b'///foo/.//bar//'), b'/foo/bar')
    self.assertEqual(posixpath.normpath(b'///foo/.//bar//.//..//.//baz'), b'/foo/baz')
    self.assertEqual(posixpath.normpath(b'///..//./foo/.//bar'), b'/foo/bar')
