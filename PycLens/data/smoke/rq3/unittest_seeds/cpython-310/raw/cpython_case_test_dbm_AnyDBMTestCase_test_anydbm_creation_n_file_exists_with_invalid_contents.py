# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm.py
# case: AnyDBMTestCase_test_anydbm_creation_n_file_exists_with_invalid_contents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_helper.create_empty_file(_fname)
    with dbm.open(_fname, 'n') as f:
        self.assertEqual(len(f), 0)
