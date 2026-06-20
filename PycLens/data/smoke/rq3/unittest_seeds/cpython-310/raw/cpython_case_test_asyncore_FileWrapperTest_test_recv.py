# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: FileWrapperTest_test_recv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    w = asyncore.file_wrapper(fd)
    os.close(fd)
    self.assertNotEqual(w.fd, fd)
    self.assertNotEqual(w.fileno(), fd)
    self.assertEqual(w.recv(13), b"It's not dead")
    self.assertEqual(w.read(6), b", it's")
    w.close()
    self.assertRaises(OSError, w.read, 1)
