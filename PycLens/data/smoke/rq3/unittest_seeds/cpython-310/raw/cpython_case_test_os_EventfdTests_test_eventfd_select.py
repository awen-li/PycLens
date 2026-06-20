# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EventfdTests_test_eventfd_select

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flags = os.EFD_CLOEXEC | os.EFD_NONBLOCK
    fd = os.eventfd(0, flags)
    self.assertNotEqual(fd, -1)
    self.addCleanup(os.close, fd)
    (rfd, wfd, xfd) = select.select([fd], [fd], [fd], 0)
    self.assertEqual((rfd, wfd, xfd), ([], [fd], []))
    os.eventfd_write(fd, 23)
    (rfd, wfd, xfd) = select.select([fd], [fd], [fd], 0)
    self.assertEqual((rfd, wfd, xfd), ([fd], [fd], []))
    self.assertEqual(os.eventfd_read(fd), 23)
    os.eventfd_write(fd, 2 ** 64 - 2)
    (rfd, wfd, xfd) = select.select([fd], [fd], [fd], 0)
    self.assertEqual((rfd, wfd, xfd), ([fd], [], []))
    os.eventfd_read(fd)
