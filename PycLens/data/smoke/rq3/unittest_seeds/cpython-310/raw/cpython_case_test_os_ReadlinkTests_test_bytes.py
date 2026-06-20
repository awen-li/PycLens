# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ReadlinkTests_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.symlink(self.filelinkb_target, self.filelinkb)
    self.addCleanup(os_helper.unlink, self.filelinkb)
    path = os.readlink(self.filelinkb)
    self.assertPathEqual(path, self.filelinkb_target)
    self.assertIsInstance(path, bytes)
