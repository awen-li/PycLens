# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_get_set_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd)
    self.assertEqual(os.get_inheritable(fd), False)
    os.set_inheritable(fd, True)
    self.assertEqual(os.get_inheritable(fd), True)
