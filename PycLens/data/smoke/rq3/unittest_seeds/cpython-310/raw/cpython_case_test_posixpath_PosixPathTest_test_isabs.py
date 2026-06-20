# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_isabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(posixpath.isabs(''), False)
    self.assertIs(posixpath.isabs('/'), True)
    self.assertIs(posixpath.isabs('/foo'), True)
    self.assertIs(posixpath.isabs('/foo/bar'), True)
    self.assertIs(posixpath.isabs('foo/bar'), False)
    self.assertIs(posixpath.isabs(b''), False)
    self.assertIs(posixpath.isabs(b'/'), True)
    self.assertIs(posixpath.isabs(b'/foo'), True)
    self.assertIs(posixpath.isabs(b'/foo/bar'), True)
    self.assertIs(posixpath.isabs(b'foo/bar'), False)
