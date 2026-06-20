# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: MsiDatabaseTestCase_test_FCICreate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filepath = TESTFN + '.txt'
    cabpath = TESTFN + '.cab'
    self.addCleanup(unlink, filepath)
    with open(filepath, 'wb'):
        pass
    self.addCleanup(unlink, cabpath)
    msilib.FCICreate(cabpath, [(filepath, 'test.txt')])
    self.assertTrue(os.path.isfile(cabpath))
