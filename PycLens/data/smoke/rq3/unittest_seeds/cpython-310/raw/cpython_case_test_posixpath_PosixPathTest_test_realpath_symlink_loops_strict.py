# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_symlink_loops_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(ABSTFN, ABSTFN)
        self.assertRaises(OSError, realpath, ABSTFN, strict=True)
        os.symlink(ABSTFN + '1', ABSTFN + '2')
        os.symlink(ABSTFN + '2', ABSTFN + '1')
        self.assertRaises(OSError, realpath, ABSTFN + '1', strict=True)
        self.assertRaises(OSError, realpath, ABSTFN + '2', strict=True)
        self.assertRaises(OSError, realpath, ABSTFN + '1/x', strict=True)
        self.assertRaises(OSError, realpath, ABSTFN + '1/..', strict=True)
        self.assertRaises(OSError, realpath, ABSTFN + '1/../x', strict=True)
        os.symlink(ABSTFN + 'x', ABSTFN + 'y')
        self.assertRaises(OSError, realpath, ABSTFN + '1/../' + basename(ABSTFN) + 'y', strict=True)
        self.assertRaises(OSError, realpath, ABSTFN + '1/../' + basename(ABSTFN) + '1', strict=True)
        os.symlink(basename(ABSTFN) + 'a/b', ABSTFN + 'a')
        self.assertRaises(OSError, realpath, ABSTFN + 'a', strict=True)
        os.symlink('../' + basename(dirname(ABSTFN)) + '/' + basename(ABSTFN) + 'c', ABSTFN + 'c')
        self.assertRaises(OSError, realpath, ABSTFN + 'c', strict=True)
        with os_helper.change_cwd(dirname(ABSTFN)):
            self.assertRaises(OSError, realpath, basename(ABSTFN), strict=True)
    finally:
        os_helper.unlink(ABSTFN)
        os_helper.unlink(ABSTFN + '1')
        os_helper.unlink(ABSTFN + '2')
        os_helper.unlink(ABSTFN + 'y')
        os_helper.unlink(ABSTFN + 'c')
        os_helper.unlink(ABSTFN + 'a')
