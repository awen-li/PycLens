# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_symlink_loops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(ABSTFN, ABSTFN)
        self.assertEqual(realpath(ABSTFN), ABSTFN)
        os.symlink(ABSTFN + '1', ABSTFN + '2')
        os.symlink(ABSTFN + '2', ABSTFN + '1')
        self.assertEqual(realpath(ABSTFN + '1'), ABSTFN + '1')
        self.assertEqual(realpath(ABSTFN + '2'), ABSTFN + '2')
        self.assertEqual(realpath(ABSTFN + '1/x'), ABSTFN + '1/x')
        self.assertEqual(realpath(ABSTFN + '1/..'), dirname(ABSTFN))
        self.assertEqual(realpath(ABSTFN + '1/../x'), dirname(ABSTFN) + '/x')
        os.symlink(ABSTFN + 'x', ABSTFN + 'y')
        self.assertEqual(realpath(ABSTFN + '1/../' + basename(ABSTFN) + 'y'), ABSTFN + 'y')
        self.assertEqual(realpath(ABSTFN + '1/../' + basename(ABSTFN) + '1'), ABSTFN + '1')
        os.symlink(basename(ABSTFN) + 'a/b', ABSTFN + 'a')
        self.assertEqual(realpath(ABSTFN + 'a'), ABSTFN + 'a/b')
        os.symlink('../' + basename(dirname(ABSTFN)) + '/' + basename(ABSTFN) + 'c', ABSTFN + 'c')
        self.assertEqual(realpath(ABSTFN + 'c'), ABSTFN + 'c')
        with os_helper.change_cwd(dirname(ABSTFN)):
            self.assertEqual(realpath(basename(ABSTFN)), ABSTFN)
    finally:
        os_helper.unlink(ABSTFN)
        os_helper.unlink(ABSTFN + '1')
        os_helper.unlink(ABSTFN + '2')
        os_helper.unlink(ABSTFN + 'y')
        os_helper.unlink(ABSTFN + 'c')
        os_helper.unlink(ABSTFN + 'a')
