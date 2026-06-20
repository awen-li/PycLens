# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_dumbdbm_creation_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        old_umask = os.umask(2)
        f = dumbdbm.open(_fname, 'c', 415)
        f.close()
    finally:
        os.umask(old_umask)
    expected_mode = 413
    if os.name != 'posix':
        expected_mode = 438
    import stat
    st = os.stat(_fname + '.dat')
    self.assertEqual(stat.S_IMODE(st.st_mode), expected_mode)
    st = os.stat(_fname + '.dir')
    self.assertEqual(stat.S_IMODE(st.st_mode), expected_mode)
