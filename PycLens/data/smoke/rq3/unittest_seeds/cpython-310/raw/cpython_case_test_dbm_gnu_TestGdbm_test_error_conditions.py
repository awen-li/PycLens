# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_error_conditions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unlink(filename)
    self.assertRaises(gdbm.error, gdbm.open, filename, 'r')
    self.g = gdbm.open(filename, 'c')
    self.g.close()
    self.assertRaises(gdbm.error, lambda : self.g['a'])
    self.assertRaises(gdbm.error, lambda : gdbm.open(filename, 'rx').close())
