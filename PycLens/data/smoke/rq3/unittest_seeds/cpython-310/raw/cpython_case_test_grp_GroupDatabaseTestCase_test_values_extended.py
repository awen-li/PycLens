# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grp.py
# case: GroupDatabaseTestCase_test_values_extended

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = grp.getgrall()
    if len(entries) > 1000:
        self.skipTest('huge group file, extended test skipped')
    for e in entries:
        e2 = grp.getgrgid(e.gr_gid)
        self.check_value(e2)
        self.assertEqual(e2.gr_gid, e.gr_gid)
        name = e.gr_name
        if name.startswith('+') or name.startswith('-'):
            continue
        e2 = grp.getgrnam(name)
        self.check_value(e2)
        self.assertEqual(e2.gr_name.lower(), name.lower())
