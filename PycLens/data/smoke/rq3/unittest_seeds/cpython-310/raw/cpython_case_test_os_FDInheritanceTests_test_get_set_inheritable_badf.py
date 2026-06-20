# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_get_set_inheritable_badf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os_helper.make_bad_fd()
    with self.assertRaises(OSError) as ctx:
        os.get_inheritable(fd)
    self.assertEqual(ctx.exception.errno, errno.EBADF)
    with self.assertRaises(OSError) as ctx:
        os.set_inheritable(fd, True)
    self.assertEqual(ctx.exception.errno, errno.EBADF)
    with self.assertRaises(OSError) as ctx:
        os.set_inheritable(fd, False)
    self.assertEqual(ctx.exception.errno, errno.EBADF)
