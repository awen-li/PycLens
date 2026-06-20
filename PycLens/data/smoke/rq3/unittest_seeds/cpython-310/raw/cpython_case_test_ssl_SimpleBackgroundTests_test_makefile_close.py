# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_makefile_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ss = test_wrap_socket(socket.socket(socket.AF_INET))
    ss.connect(self.server_addr)
    fd = ss.fileno()
    f = ss.makefile()
    f.close()
    os.read(fd, 0)
    ss.close()
    gc.collect()
    with self.assertRaises(OSError) as e:
        os.read(fd, 0)
    self.assertEqual(e.exception.errno, errno.EBADF)
