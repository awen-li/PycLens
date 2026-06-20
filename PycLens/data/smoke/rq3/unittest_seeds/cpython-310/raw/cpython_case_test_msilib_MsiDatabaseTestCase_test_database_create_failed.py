# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_database_create_failed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    db_path = os.path.join(TESTFN, 'test.msi')
    with self.assertRaises(msilib.MSIError) as cm:
        msilib.OpenDatabase(db_path, msilib.MSIDBOPEN_CREATE)
    self.assertEqual(str(cm.exception), 'create failed')
