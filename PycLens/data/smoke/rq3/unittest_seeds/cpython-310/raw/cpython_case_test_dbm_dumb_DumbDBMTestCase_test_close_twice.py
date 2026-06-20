# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_close_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = dumbdbm.open(_fname)
    f[b'a'] = b'b'
    self.assertEqual(f[b'a'], b'b')
    f.close()
    f.close()
