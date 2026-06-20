# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_nonascii_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN_NONASCII
    for suffix in ['', '.pag', '.dir', '.db']:
        self.addCleanup(os_helper.unlink, filename + suffix)
    with dbm.ndbm.open(filename, 'c') as db:
        db[b'key'] = b'value'
    self.assertTrue(any((os.path.exists(filename + suffix) for suffix in ['', '.pag', '.dir', '.db'])))
    with dbm.ndbm.open(filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'key'])
        self.assertTrue(b'key' in db)
        self.assertEqual(db[b'key'], b'value')
