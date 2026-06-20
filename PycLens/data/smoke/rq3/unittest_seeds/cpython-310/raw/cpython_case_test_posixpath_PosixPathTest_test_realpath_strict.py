# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(ABSTFN + '1', ABSTFN)
        self.assertRaises(FileNotFoundError, realpath, ABSTFN, strict=True)
        self.assertRaises(FileNotFoundError, realpath, ABSTFN + '2', strict=True)
    finally:
        os_helper.unlink(ABSTFN)
