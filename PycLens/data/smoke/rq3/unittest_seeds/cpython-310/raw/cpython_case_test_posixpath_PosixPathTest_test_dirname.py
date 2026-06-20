# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_dirname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(posixpath.dirname('/foo/bar'), '/foo')
    self.assertEqual(posixpath.dirname('/'), '/')
    self.assertEqual(posixpath.dirname('foo'), '')
    self.assertEqual(posixpath.dirname('////foo'), '////')
    self.assertEqual(posixpath.dirname('//foo//bar'), '//foo')
    self.assertEqual(posixpath.dirname(b'/foo/bar'), b'/foo')
    self.assertEqual(posixpath.dirname(b'/'), b'/')
    self.assertEqual(posixpath.dirname(b'foo'), b'')
    self.assertEqual(posixpath.dirname(b'////foo'), b'////')
    self.assertEqual(posixpath.dirname(b'//foo//bar'), b'//foo')
