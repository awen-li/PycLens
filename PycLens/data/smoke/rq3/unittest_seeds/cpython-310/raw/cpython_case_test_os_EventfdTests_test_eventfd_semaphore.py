# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EventfdTests_test_eventfd_semaphore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    initval = 2
    flags = os.EFD_CLOEXEC | os.EFD_SEMAPHORE | os.EFD_NONBLOCK
    fd = os.eventfd(initval, flags)
    self.assertNotEqual(fd, -1)
    self.addCleanup(os.close, fd)
    res = os.eventfd_read(fd)
    self.assertEqual(res, 1)
    res = os.eventfd_read(fd)
    self.assertEqual(res, 1)
    with self.assertRaises(BlockingIOError):
        os.eventfd_read(fd)
    with self.assertRaises(BlockingIOError):
        os.read(fd, 8)
    os.eventfd_write(fd, 1)
    res = os.eventfd_read(fd)
    self.assertEqual(res, 1)
    with self.assertRaises(BlockingIOError):
        os.eventfd_read(fd)
