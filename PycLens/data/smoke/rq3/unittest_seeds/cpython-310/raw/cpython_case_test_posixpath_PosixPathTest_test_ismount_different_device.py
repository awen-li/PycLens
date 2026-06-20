# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_ismount_different_device

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    save_lstat = os.lstat

    def fake_lstat(path):
        st_ino = 0
        st_dev = 0
        if path == ABSTFN:
            st_dev = 1
            st_ino = 1
        return posix.stat_result((0, st_ino, st_dev, 0, 0, 0, 0, 0, 0, 0))
    try:
        os.lstat = fake_lstat
        self.assertIs(posixpath.ismount(ABSTFN), True)
    finally:
        os.lstat = save_lstat
