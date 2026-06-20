# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_opener_invalid_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os_helper.make_bad_fd()
    with self.assertRaises(OSError) as cm:
        self.open('foo', opener=lambda name, flags: fd)
    self.assertEqual(cm.exception.errno, errno.EBADF)
