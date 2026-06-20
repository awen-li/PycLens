# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_resolve_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkdir(ABSTFN)
        os.mkdir(ABSTFN + '/y')
        os.symlink(ABSTFN + '/y', ABSTFN + '/k')
        with os_helper.change_cwd(ABSTFN + '/k'):
            self.assertEqual(realpath('a'), ABSTFN + '/y/a')
    finally:
        os_helper.unlink(ABSTFN + '/k')
        safe_rmdir(ABSTFN + '/y')
        safe_rmdir(ABSTFN)
