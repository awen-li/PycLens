# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ReadlinkTests_test_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.symlink(self.filelink_target, self.filelink)
    self.addCleanup(os_helper.unlink, self.filelink)
    filelink = FakePath(self.filelink)
    self.assertPathEqual(os.readlink(filelink), self.filelink_target)
