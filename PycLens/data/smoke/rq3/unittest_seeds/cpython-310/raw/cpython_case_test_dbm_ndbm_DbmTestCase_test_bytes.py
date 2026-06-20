# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dbm.ndbm.open(self.filename, 'c') as db:
        db[b'bytes key \xbd'] = b'bytes value \xbd'
    with dbm.ndbm.open(self.filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'bytes key \xbd'])
        self.assertTrue(b'bytes key \xbd' in db)
        self.assertEqual(db[b'bytes key \xbd'], b'bytes value \xbd')
