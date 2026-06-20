# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ReadlinkTests_test_not_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filelink_target = FakePath(self.filelink_target)
    self.assertRaises(OSError, os.readlink, self.filelink_target)
    self.assertRaises(OSError, os.readlink, filelink_target)
