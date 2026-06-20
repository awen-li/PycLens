# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32JunctionTests_test_create_junction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _winapi.CreateJunction(self.junction_target, self.junction)
    self.assertTrue(os.path.lexists(self.junction))
    self.assertTrue(os.path.exists(self.junction))
    self.assertTrue(os.path.isdir(self.junction))
    self.assertNotEqual(os.stat(self.junction), os.lstat(self.junction))
    self.assertEqual(os.stat(self.junction), os.stat(self.junction_target))
    self.assertFalse(os.path.islink(self.junction))
    self.assertEqual(os.path.normcase('\\\\?\\' + self.junction_target), os.path.normcase(os.readlink(self.junction)))
