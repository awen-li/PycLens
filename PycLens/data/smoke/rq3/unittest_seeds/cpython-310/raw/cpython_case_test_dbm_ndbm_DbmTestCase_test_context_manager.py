# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dbm.ndbm.open(self.filename, 'c') as db:
        db['ndbm context manager'] = 'context manager'
    with dbm.ndbm.open(self.filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'ndbm context manager'])
    with self.assertRaises(dbm.ndbm.error) as cm:
        db.keys()
    self.assertEqual(str(cm.exception), 'DBM object has already been closed')
