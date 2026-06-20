# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_dup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd1 = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd1)
    fd2 = os.dup(fd1)
    self.addCleanup(os.close, fd2)
    self.assertEqual(os.get_inheritable(fd2), False)
