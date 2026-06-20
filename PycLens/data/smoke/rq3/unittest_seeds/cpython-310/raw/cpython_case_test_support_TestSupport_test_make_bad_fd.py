# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_make_bad_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os_helper.make_bad_fd()
    with self.assertRaises(OSError) as cm:
        os.write(fd, b'foo')
    self.assertEqual(cm.exception.errno, errno.EBADF)
