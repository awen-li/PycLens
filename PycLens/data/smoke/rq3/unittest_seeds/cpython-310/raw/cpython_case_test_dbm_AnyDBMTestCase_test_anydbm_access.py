# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_anydbm_access

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    f = dbm.open(_fname, 'r')
    key = 'a'.encode('ascii')
    self.assertIn(key, f)
    assert f[key] == b'Python:'
    f.close()
