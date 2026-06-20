# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ChownFileTests_test_chown_uid_gid_arguments_must_be_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stat = os.stat(os_helper.TESTFN)
    uid = stat.st_uid
    gid = stat.st_gid
    for value in (-1.0, -1j, decimal.Decimal(-1), fractions.Fraction(-2, 2)):
        self.assertRaises(TypeError, os.chown, os_helper.TESTFN, value, gid)
        self.assertRaises(TypeError, os.chown, os_helper.TESTFN, uid, value)
    self.assertIsNone(os.chown(os_helper.TESTFN, uid, gid))
    self.assertIsNone(os.chown(os_helper.TESTFN, -1, -1))
