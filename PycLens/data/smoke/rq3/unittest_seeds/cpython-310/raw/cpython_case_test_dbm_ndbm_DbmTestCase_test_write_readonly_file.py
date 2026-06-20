# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_write_readonly_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with dbm.ndbm.open(self.filename, 'c') as db:
        db[b'bytes key'] = b'bytes value'
    with dbm.ndbm.open(self.filename, 'r') as db:
        with self.assertRaises(error):
            del db[b'not exist key']
        with self.assertRaises(error):
            del db[b'bytes key']
        with self.assertRaises(error):
            db[b'not exist key'] = b'not exist value'
