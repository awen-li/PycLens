# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_invalid_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flag in ('x', 'rf', None):
        with self.assertRaisesRegex(ValueError, "Flag must be one of 'r', 'w', 'c', or 'n'"):
            dumbdbm.open(_fname, flag)
