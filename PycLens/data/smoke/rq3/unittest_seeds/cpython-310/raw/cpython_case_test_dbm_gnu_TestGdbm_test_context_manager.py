# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gdbm.open(filename, 'c') as db:
        db['gdbm context manager'] = 'context manager'
    with gdbm.open(filename, 'r') as db:
        self.assertEqual(list(db.keys()), [b'gdbm context manager'])
    with self.assertRaises(gdbm.error) as cm:
        db.keys()
    self.assertEqual(str(cm.exception), 'GDBM object has already been closed')
