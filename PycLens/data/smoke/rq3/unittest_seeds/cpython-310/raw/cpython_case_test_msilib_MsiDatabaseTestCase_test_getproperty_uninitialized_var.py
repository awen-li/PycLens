# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_getproperty_uninitialized_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    self.addCleanup(unlink, db_path)
    self.addCleanup(db.Close)
    si = db.GetSummaryInformation(0)
    with self.assertRaises(msilib.MSIError):
        si.GetProperty(-1)
