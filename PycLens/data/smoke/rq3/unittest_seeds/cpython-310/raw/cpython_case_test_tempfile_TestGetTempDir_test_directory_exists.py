# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetTempDir_test_directory_exists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in (tempfile.gettempdir(), tempfile.gettempdirb()):
        self.assertTrue(os.path.isabs(d) or d == os.curdir, '%r is not an absolute path' % d)
        self.assertTrue(os.path.isdir(d), '%r is not a directory' % d)
