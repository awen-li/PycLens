# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MakedirTests_test_exist_ok_s_isgid_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(os_helper.TESTFN, 'dir1')
    S_ISGID = stat.S_ISGID
    mode = 511
    old_mask = os.umask(18)
    try:
        existing_testfn_mode = stat.S_IMODE(os.lstat(os_helper.TESTFN).st_mode)
        try:
            os.chmod(os_helper.TESTFN, existing_testfn_mode | S_ISGID)
        except PermissionError:
            raise unittest.SkipTest('Cannot set S_ISGID for dir.')
        if os.lstat(os_helper.TESTFN).st_mode & S_ISGID != S_ISGID:
            raise unittest.SkipTest('No support for S_ISGID dir mode.')
        os.makedirs(path, mode | S_ISGID)
        os.makedirs(path, mode, exist_ok=True)
        os.chmod(path, stat.S_IMODE(os.lstat(path).st_mode) & ~S_ISGID)
        os.makedirs(path, mode | S_ISGID, exist_ok=True)
    finally:
        os.umask(old_mask)
