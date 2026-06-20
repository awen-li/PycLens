# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_symlink_loops

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
    self.assertPathEqual(ntpath.realpath(ABSTFN), ABSTFN)
    os.symlink(ABSTFN + '1', ABSTFN + '2')
    os.symlink(ABSTFN + '2', ABSTFN + '1')
    expected = (ABSTFN + '1', ABSTFN + '2')
    self.assertPathIn(ntpath.realpath(ABSTFN + '1'), expected)
    self.assertPathIn(ntpath.realpath(ABSTFN + '2'), expected)
    self.assertPathIn(ntpath.realpath(ABSTFN + '1\\x'), (ntpath.join(r, 'x') for r in expected))
    self.assertPathEqual(ntpath.realpath(ABSTFN + '1\\..'), ntpath.dirname(ABSTFN))
    self.assertPathEqual(ntpath.realpath(ABSTFN + '1\\..\\x'), ntpath.dirname(ABSTFN) + '\\x')
    os.symlink(ABSTFN + 'x', ABSTFN + 'y')
    self.assertPathEqual(ntpath.realpath(ABSTFN + '1\\..\\' + ntpath.basename(ABSTFN) + 'y'), ABSTFN + 'x')
    self.assertPathIn(ntpath.realpath(ABSTFN + '1\\..\\' + ntpath.basename(ABSTFN) + '1'), expected)
    os.symlink(ntpath.basename(ABSTFN) + 'a\\b', ABSTFN + 'a')
    self.assertPathEqual(ntpath.realpath(ABSTFN + 'a'), ABSTFN + 'a')
    os.symlink('..\\' + ntpath.basename(ntpath.dirname(ABSTFN)) + '\\' + ntpath.basename(ABSTFN) + 'c', ABSTFN + 'c')
    self.assertPathEqual(ntpath.realpath(ABSTFN + 'c'), ABSTFN + 'c')
    self.assertPathEqual(ntpath.realpath(ntpath.basename(ABSTFN)), ABSTFN)
