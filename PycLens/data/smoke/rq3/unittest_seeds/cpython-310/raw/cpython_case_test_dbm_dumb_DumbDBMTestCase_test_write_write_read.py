# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_write_write_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with contextlib.closing(dumbdbm.open(_fname)) as f:
        f[b'1'] = b'hello'
        f[b'1'] = b'hello2'
    with contextlib.closing(dumbdbm.open(_fname)) as f:
        self.assertEqual(f[b'1'], b'hello2')
