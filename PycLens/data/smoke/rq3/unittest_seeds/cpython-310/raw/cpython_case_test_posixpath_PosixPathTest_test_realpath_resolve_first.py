# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_resolve_first

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkdir(ABSTFN)
        os.mkdir(ABSTFN + '/k')
        os.symlink(ABSTFN, ABSTFN + 'link')
        with os_helper.change_cwd(dirname(ABSTFN)):
            base = basename(ABSTFN)
            self.assertEqual(realpath(base + 'link'), ABSTFN)
            self.assertEqual(realpath(base + 'link/k'), ABSTFN + '/k')
    finally:
        os_helper.unlink(ABSTFN + 'link')
        safe_rmdir(ABSTFN + '/k')
        safe_rmdir(ABSTFN)
