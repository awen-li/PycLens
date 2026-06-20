# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_dumbdbm_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.init_db()
    with contextlib.closing(dumbdbm.open(_fname)) as f:
        keys = self.keys_helper(f)
