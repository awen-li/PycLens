# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_ndbm.py
# case: DbmTestCase_test_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for mode in ['r', 'rw', 'w', 'n']:
        try:
            self.d = dbm.ndbm.open(self.filename, mode)
            self.d.close()
        except error:
            self.fail()
