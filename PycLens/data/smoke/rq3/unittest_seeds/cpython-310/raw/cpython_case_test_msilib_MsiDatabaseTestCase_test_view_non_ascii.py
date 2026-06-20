# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_view_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    view = db.OpenView("SELECT 'ß-розпад' FROM Property")
    view.Execute(None)
    record = view.Fetch()
    self.assertEqual(record.GetString(1), 'ß-розпад')
    view.Close()
    db.Close()
    self.addCleanup(unlink, db_path)
