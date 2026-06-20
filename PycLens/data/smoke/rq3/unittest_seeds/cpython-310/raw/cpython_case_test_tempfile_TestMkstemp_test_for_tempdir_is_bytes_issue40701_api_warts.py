# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstemp_test_for_tempdir_is_bytes_issue40701_api_warts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_tempdir = tempfile.tempdir
    self.assertIsInstance(tempfile.tempdir, (str, type(None)))
    try:
        (fd, path) = tempfile.mkstemp()
        os.close(fd)
        os.unlink(path)
        self.assertIsInstance(path, str)
        tempfile.tempdir = tempfile.gettempdirb()
        self.assertIsInstance(tempfile.tempdir, bytes)
        self.assertIsInstance(tempfile.gettempdir(), str)
        self.assertIsInstance(tempfile.gettempdirb(), bytes)
        (fd, path) = tempfile.mkstemp()
        os.close(fd)
        os.unlink(path)
        self.assertIsInstance(path, bytes)
        (fd, path) = tempfile.mkstemp(suffix='.txt')
        os.close(fd)
        os.unlink(path)
        self.assertIsInstance(path, str)
        (fd, path) = tempfile.mkstemp(prefix='test-temp-')
        os.close(fd)
        os.unlink(path)
        self.assertIsInstance(path, str)
        (fd, path) = tempfile.mkstemp(dir=tempfile.gettempdir())
        os.close(fd)
        os.unlink(path)
        self.assertIsInstance(path, str)
    finally:
        tempfile.tempdir = orig_tempdir
