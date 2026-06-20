# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_directory_start_component_keyfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (db, db_path) = init_database()
    self.addCleanup(unlink, db_path)
    self.addCleanup(db.Close)
    self.addCleanup(msilib._directories.clear)
    feature = msilib.Feature(db, 0, 'Feature', 'A feature', 'Python')
    cab = msilib.CAB('CAB')
    dir = msilib.Directory(db, cab, None, TESTFN, 'TARGETDIR', 'SourceDir', 0)
    dir.start_component(None, feature, None, 'keyfile')
