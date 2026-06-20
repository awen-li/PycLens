# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grp.py
# case: GroupDatabaseTestCase_test_noninteger_gid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = grp.getgrall()
    if not entries:
        self.skipTest('no groups')
    gid = entries[0][2]
    self.assertRaises(TypeError, grp.getgrgid, float(gid))
    self.assertRaises(TypeError, grp.getgrgid, str(gid))
