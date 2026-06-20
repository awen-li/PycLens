# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_ismount_non_existent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(posixpath.ismount(ABSTFN), False)
    try:
        os.mkdir(ABSTFN)
        self.assertIs(posixpath.ismount(ABSTFN), False)
    finally:
        safe_rmdir(ABSTFN)
    self.assertIs(posixpath.ismount('/\udfff'), False)
    self.assertIs(posixpath.ismount(b'/\xff'), False)
    self.assertIs(posixpath.ismount('/\x00'), False)
    self.assertIs(posixpath.ismount(b'/\x00'), False)
