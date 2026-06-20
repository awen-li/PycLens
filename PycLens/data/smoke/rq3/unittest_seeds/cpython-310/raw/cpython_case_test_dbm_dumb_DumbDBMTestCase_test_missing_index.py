# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_missing_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dumbdbm.open(_fname, 'n') as f:
        pass
    os.unlink(_fname + '.dir')
    for value in ('r', 'w'):
        with self.assertRaises(FileNotFoundError):
            dumbdbm.open(_fname, value)
        self.assertFalse(os.path.exists(_fname + '.dir'))
        self.assertFalse(os.path.exists(_fname + '.bak'))
