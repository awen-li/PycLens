# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_get_property_vt_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    summary = db.GetSummaryInformation(0)
    self.assertIsNone(summary.GetProperty(msilib.PID_SECURITY))
    db.Close()
    self.addCleanup(unlink, db_path)
