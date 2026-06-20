# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_nonascii_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = TESTFN_NONASCII
    self.addCleanup(unlink, filename)
    with gdbm.open(filename, 'c') as db:
        db[b'key'] = b'value'
    self.assertTrue(os.path.exists(filename))
    with gdbm.open(filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'key'])
        self.assertTrue(b'key' in db)
        self.assertEqual(db[b'key'], b'value')
