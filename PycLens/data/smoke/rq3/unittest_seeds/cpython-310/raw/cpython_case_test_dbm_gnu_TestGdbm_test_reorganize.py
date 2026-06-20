# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_reorganize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.g = gdbm.open(filename, 'c')
    size0 = os.path.getsize(filename)
    value_size = max(size0, 10000)
    self.g['x'] = 'x' * value_size
    size1 = os.path.getsize(filename)
    self.assertGreater(size1, size0)
    del self.g['x']
    self.assertEqual(os.path.getsize(filename), size1)
    self.g.reorganize()
    size2 = os.path.getsize(filename)
    self.assertLess(size2, size1)
    self.assertGreaterEqual(size2, size0)
