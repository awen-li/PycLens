# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_ismount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(posixpath.ismount('/'), True)
    self.assertIs(posixpath.ismount(b'/'), True)
    self.assertIs(posixpath.ismount(FakePath('/')), True)
    self.assertIs(posixpath.ismount(FakePath(b'/')), True)
