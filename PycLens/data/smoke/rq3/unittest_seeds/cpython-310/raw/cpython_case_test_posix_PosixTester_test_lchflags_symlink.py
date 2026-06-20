# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_lchflags_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testfn_st = os.stat(os_helper.TESTFN)
    self.assertTrue(hasattr(testfn_st, 'st_flags'))
    os.symlink(os_helper.TESTFN, _DUMMY_SYMLINK)
    self.teardown_files.append(_DUMMY_SYMLINK)
    dummy_symlink_st = os.lstat(_DUMMY_SYMLINK)

    def chflags_nofollow(path, flags):
        return posix.chflags(path, flags, follow_symlinks=False)
    for fn in (posix.lchflags, chflags_nofollow):
        flags = dummy_symlink_st.st_flags | stat.UF_IMMUTABLE
        try:
            fn(_DUMMY_SYMLINK, flags)
        except OSError as err:
            if err.errno != errno.EOPNOTSUPP:
                raise
            msg = 'chflag UF_IMMUTABLE not supported by underlying fs'
            self.skipTest(msg)
        try:
            new_testfn_st = os.stat(os_helper.TESTFN)
            new_dummy_symlink_st = os.lstat(_DUMMY_SYMLINK)
            self.assertEqual(testfn_st.st_flags, new_testfn_st.st_flags)
            self.assertEqual(dummy_symlink_st.st_flags | stat.UF_IMMUTABLE, new_dummy_symlink_st.st_flags)
        finally:
            fn(_DUMMY_SYMLINK, dummy_symlink_st.st_flags)
