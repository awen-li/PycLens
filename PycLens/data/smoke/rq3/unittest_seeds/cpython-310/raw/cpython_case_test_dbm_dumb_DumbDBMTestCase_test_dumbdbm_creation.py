# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_dumbdbm_creation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with contextlib.closing(dumbdbm.open(_fname, 'c')) as f:
        self.assertEqual(list(f.keys()), [])
        for key in self._dict:
            f[key] = self._dict[key]
        self.read_helper(f)
