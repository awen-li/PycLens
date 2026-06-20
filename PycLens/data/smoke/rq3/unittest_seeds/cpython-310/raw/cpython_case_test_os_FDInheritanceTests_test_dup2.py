# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_dup2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd)
    fd2 = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd2)
    self.assertEqual(os.dup2(fd, fd2), fd2)
    self.assertTrue(os.get_inheritable(fd2))
    fd3 = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd3)
    self.assertEqual(os.dup2(fd, fd3, inheritable=False), fd3)
    self.assertFalse(os.get_inheritable(fd3))
