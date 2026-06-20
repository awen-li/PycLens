# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32JunctionTests_test_unlink_removes_junction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _winapi.CreateJunction(self.junction_target, self.junction)
    self.assertTrue(os.path.exists(self.junction))
    self.assertTrue(os.path.lexists(self.junction))
    os.unlink(self.junction)
    self.assertFalse(os.path.exists(self.junction))
