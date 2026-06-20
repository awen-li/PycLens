# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_anydbm_creation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = dbm.open(_fname, 'c')
    self.assertEqual(list(f.keys()), [])
    for key in self._dict:
        f[key.encode('ascii')] = self._dict[key]
    self.read_helper(f)
    f.close()
