# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_nonexisting_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nonexisting_file = 'nonexisting-file'
    with self.assertRaises(dbm.ndbm.error) as cm:
        dbm.ndbm.open(nonexisting_file)
    self.assertIn(nonexisting_file, str(cm.exception))
    self.assertEqual(cm.exception.filename, nonexisting_file)
