# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_openpty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (master_fd, slave_fd) = os.openpty()
    self.addCleanup(os.close, master_fd)
    self.addCleanup(os.close, slave_fd)
    self.assertEqual(os.get_inheritable(master_fd), False)
    self.assertEqual(os.get_inheritable(slave_fd), False)
