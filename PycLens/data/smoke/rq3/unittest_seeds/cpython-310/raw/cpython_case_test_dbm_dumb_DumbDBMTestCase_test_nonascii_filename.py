# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_nonascii_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN_NONASCII
    for suffix in ['.dir', '.dat', '.bak']:
        self.addCleanup(os_helper.unlink, filename + suffix)
    with dumbdbm.open(filename, 'c') as db:
        db[b'key'] = b'value'
    self.assertTrue(os.path.exists(filename + '.dat'))
    self.assertTrue(os.path.exists(filename + '.dir'))
    with dumbdbm.open(filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'key'])
        self.assertTrue(b'key' in db)
        self.assertEqual(db[b'key'], b'value')
