# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: FileWrapperTest_test_close_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    f = asyncore.file_wrapper(fd)
    os.close(fd)
    os.close(f.fd)
    with self.assertRaises(OSError):
        f.close()
    self.assertEqual(f.fd, -1)
    f.close()
