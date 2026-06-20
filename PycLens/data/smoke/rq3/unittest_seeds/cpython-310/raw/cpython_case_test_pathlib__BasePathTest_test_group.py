# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'fileA'
    gid = p.stat().st_gid
    try:
        name = grp.getgrgid(gid).gr_name
    except KeyError:
        self.skipTest("group %d doesn't have an entry in the system database" % gid)
    self.assertEqual(name, p.group())
