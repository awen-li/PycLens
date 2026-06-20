# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestInvalidFD_test_closerange

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os_helper.make_bad_fd()
    for i in range(10):
        try:
            os.fstat(fd + i)
        except OSError:
            pass
        else:
            break
    if i < 2:
        raise unittest.SkipTest('Unable to acquire a range of invalid file descriptors')
    self.assertEqual(os.closerange(fd, fd + i - 1), None)
