# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ChownFileTests_test_chown_gid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    groups = os.getgroups()
    if len(groups) < 2:
        self.skipTest('test needs at least 2 groups')
    (gid_1, gid_2) = groups[:2]
    uid = os.stat(os_helper.TESTFN).st_uid
    os.chown(os_helper.TESTFN, uid, gid_1)
    gid = os.stat(os_helper.TESTFN).st_gid
    self.assertEqual(gid, gid_1)
    os.chown(os_helper.TESTFN, uid, gid_2)
    gid = os.stat(os_helper.TESTFN).st_gid
    self.assertEqual(gid, gid_2)
