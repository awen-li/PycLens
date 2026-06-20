# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestInvalidFD_test_dup2_negative_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    valid_fd = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, valid_fd)
    fds = [valid_fd, -1, -2 ** 31]
    for (fd, fd2) in itertools.product(fds, repeat=2):
        if fd != fd2:
            with self.subTest(fd=fd, fd2=fd2):
                with self.assertRaises(OSError) as ctx:
                    os.dup2(fd, fd2)
                self.assertEqual(ctx.exception.errno, errno.EBADF)
