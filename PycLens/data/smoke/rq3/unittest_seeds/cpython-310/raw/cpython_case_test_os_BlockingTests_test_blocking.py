# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: BlockingTests_test_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd)
    self.assertEqual(os.get_blocking(fd), True)
    os.set_blocking(fd, False)
    self.assertEqual(os.get_blocking(fd), False)
    os.set_blocking(fd, True)
    self.assertEqual(os.get_blocking(fd), True)
