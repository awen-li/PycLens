# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_write_readonly_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gdbm.open(filename, 'c') as db:
        db[b'bytes key'] = b'bytes value'
    with gdbm.open(filename, 'r') as db:
        with self.assertRaises(gdbm.error):
            del db[b'not exist key']
        with self.assertRaises(gdbm.error):
            del db[b'bytes key']
        with self.assertRaises(gdbm.error):
            db[b'not exist key'] = b'not exist value'
