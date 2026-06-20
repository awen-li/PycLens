# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_resolve_before_normalizing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkdir(ABSTFN)
        os.mkdir(ABSTFN + '/k')
        os.mkdir(ABSTFN + '/k/y')
        os.symlink(ABSTFN + '/k/y', ABSTFN + '/link-y')
        self.assertEqual(realpath(ABSTFN + '/link-y/..'), ABSTFN + '/k')
        with os_helper.change_cwd(dirname(ABSTFN)):
            self.assertEqual(realpath(basename(ABSTFN) + '/link-y/..'), ABSTFN + '/k')
    finally:
        os_helper.unlink(ABSTFN + '/link-y')
        safe_rmdir(ABSTFN + '/k/y')
        safe_rmdir(ABSTFN + '/k')
        safe_rmdir(ABSTFN)
