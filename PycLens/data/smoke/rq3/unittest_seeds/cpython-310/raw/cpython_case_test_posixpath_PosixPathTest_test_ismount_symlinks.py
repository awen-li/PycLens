# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_ismount_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink('/', ABSTFN)
        self.assertIs(posixpath.ismount(ABSTFN), False)
    finally:
        os.unlink(ABSTFN)
