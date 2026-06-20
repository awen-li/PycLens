# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_symlink_loops_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    self.addCleanup(os_helper.unlink, ABSTFN)
    self.addCleanup(os_helper.unlink, ABSTFN + '1')
    self.addCleanup(os_helper.unlink, ABSTFN + '2')
    self.addCleanup(os_helper.unlink, ABSTFN + 'y')
    self.addCleanup(os_helper.unlink, ABSTFN + 'c')
    self.addCleanup(os_helper.unlink, ABSTFN + 'a')
    os.symlink(ABSTFN, ABSTFN)
    self.assertRaises(OSError, ntpath.realpath, ABSTFN, strict=True)
    os.symlink(ABSTFN + '1', ABSTFN + '2')
    os.symlink(ABSTFN + '2', ABSTFN + '1')
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '1', strict=True)
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '2', strict=True)
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '1\\x', strict=True)
    self.assertPathEqual(ntpath.realpath(ABSTFN + '1\\..', strict=True), ntpath.dirname(ABSTFN))
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '1\\..\\x', strict=True)
    os.symlink(ABSTFN + 'x', ABSTFN + 'y')
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '1\\..\\' + ntpath.basename(ABSTFN) + 'y', strict=True)
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + '1\\..\\' + ntpath.basename(ABSTFN) + '1', strict=True)
    os.symlink(ntpath.basename(ABSTFN) + 'a\\b', ABSTFN + 'a')
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + 'a', strict=True)
    os.symlink('..\\' + ntpath.basename(ntpath.dirname(ABSTFN)) + '\\' + ntpath.basename(ABSTFN) + 'c', ABSTFN + 'c')
    self.assertRaises(OSError, ntpath.realpath, ABSTFN + 'c', strict=True)
    self.assertRaises(OSError, ntpath.realpath, ntpath.basename(ABSTFN), strict=True)
