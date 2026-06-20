# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_summaryinfo_getproperty_issue1104

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    try:
        sum_info = db.GetSummaryInformation(99)
        title = sum_info.GetProperty(msilib.PID_TITLE)
        self.assertEqual(title, b'Installation Database')
        sum_info.SetProperty(msilib.PID_TITLE, 'a' * 999)
        title = sum_info.GetProperty(msilib.PID_TITLE)
        self.assertEqual(title, b'a' * 999)
        sum_info.SetProperty(msilib.PID_TITLE, 'a' * 1000)
        title = sum_info.GetProperty(msilib.PID_TITLE)
        self.assertEqual(title, b'a' * 1000)
        sum_info.SetProperty(msilib.PID_TITLE, 'a' * 1001)
        title = sum_info.GetProperty(msilib.PID_TITLE)
        self.assertEqual(title, b'a' * 1001)
    finally:
        db = None
        sum_info = None
        os.unlink(db_path)
