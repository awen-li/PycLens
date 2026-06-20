# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MemfdCreateTests_test_memfd_create

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.memfd_create('Hi', os.MFD_CLOEXEC)
    self.assertNotEqual(fd, -1)
    self.addCleanup(os.close, fd)
    self.assertFalse(os.get_inheritable(fd))
    with open(fd, 'wb', closefd=False) as f:
        f.write(b'memfd_create')
        self.assertEqual(f.tell(), 12)
    fd2 = os.memfd_create('Hi')
    self.addCleanup(os.close, fd2)
    self.assertFalse(os.get_inheritable(fd2))
