# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dumbdbm.open(_fname, 'c') as db:
        db['dumbdbm context manager'] = 'context manager'
    with dumbdbm.open(_fname, 'r') as db:
        self.assertEqual(list(db.keys()), [b'dumbdbm context manager'])
    with self.assertRaises(dumbdbm.error):
        db.keys()
