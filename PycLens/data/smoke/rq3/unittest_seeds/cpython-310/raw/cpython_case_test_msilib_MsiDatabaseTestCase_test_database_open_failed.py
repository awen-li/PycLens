# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_database_open_failed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(msilib.MSIError) as cm:
        msilib.OpenDatabase('non-existent.msi', msilib.MSIDBOPEN_READONLY)
    self.assertEqual(str(cm.exception), 'open failed')
