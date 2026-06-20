# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ChownFileTests_test_chown_without_permission

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (uid_1, uid_2) = all_users[:2]
    gid = os.stat(os_helper.TESTFN).st_gid
    with self.assertRaises(PermissionError):
        os.chown(os_helper.TESTFN, uid_1, gid)
        os.chown(os_helper.TESTFN, uid_2, gid)
