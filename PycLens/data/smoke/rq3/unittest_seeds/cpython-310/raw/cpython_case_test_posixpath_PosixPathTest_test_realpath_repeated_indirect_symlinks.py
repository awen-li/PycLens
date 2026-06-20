# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_repeated_indirect_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkdir(ABSTFN)
        os.symlink('../' + basename(ABSTFN), ABSTFN + '/self')
        os.symlink('self/self/self', ABSTFN + '/link')
        self.assertEqual(realpath(ABSTFN + '/link'), ABSTFN)
    finally:
        os_helper.unlink(ABSTFN + '/self')
        os_helper.unlink(ABSTFN + '/link')
        safe_rmdir(ABSTFN)
