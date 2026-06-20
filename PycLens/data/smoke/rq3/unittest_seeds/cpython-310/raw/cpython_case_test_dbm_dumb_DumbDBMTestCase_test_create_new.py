# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_create_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dumbdbm.open(_fname, 'n') as f:
        for k in self._dict:
            f[k] = self._dict[k]
    with dumbdbm.open(_fname, 'n') as f:
        self.assertEqual(f.keys(), [])
