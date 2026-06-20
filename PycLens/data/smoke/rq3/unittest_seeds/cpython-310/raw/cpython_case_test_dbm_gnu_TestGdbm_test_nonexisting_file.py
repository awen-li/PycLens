# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_nonexisting_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nonexisting_file = 'nonexisting-file'
    with self.assertRaises(gdbm.error) as cm:
        gdbm.open(nonexisting_file)
    self.assertIn(nonexisting_file, str(cm.exception))
    self.assertEqual(cm.exception.filename, nonexisting_file)
