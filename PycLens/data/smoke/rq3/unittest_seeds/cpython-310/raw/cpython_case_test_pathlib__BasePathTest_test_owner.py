# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_owner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE) / 'fileA'
    uid = p.stat().st_uid
    try:
        name = pwd.getpwuid(uid).pw_name
    except KeyError:
        self.skipTest("user %d doesn't have an entry in the system database" % uid)
    self.assertEqual(name, p.owner())
