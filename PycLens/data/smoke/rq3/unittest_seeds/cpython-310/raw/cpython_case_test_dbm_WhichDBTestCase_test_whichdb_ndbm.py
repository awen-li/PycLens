# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: WhichDBTestCase_test_whichdb_ndbm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(_fname + '.db', 'wb'):
        pass
    self.assertIsNone(self.dbm.whichdb(_fname))
