# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_view_fetch_returns_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    properties = []
    view = db.OpenView('SELECT Property, Value FROM Property')
    view.Execute(None)
    while True:
        record = view.Fetch()
        if record is None:
            break
        properties.append(record.GetString(1))
    view.Close()
    db.Close()
    self.assertEqual(properties, ['ProductName', 'ProductCode', 'ProductVersion', 'Manufacturer', 'ProductLanguage'])
    self.addCleanup(unlink, db_path)
