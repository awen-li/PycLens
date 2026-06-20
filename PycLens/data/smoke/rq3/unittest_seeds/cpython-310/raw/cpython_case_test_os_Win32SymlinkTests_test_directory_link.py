# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_directory_link

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.symlink(self.dirlink_target, self.dirlink)
    self.assertTrue(os.path.exists(self.dirlink))
    self.assertTrue(os.path.isdir(self.dirlink))
    self.assertTrue(os.path.islink(self.dirlink))
    self.check_stat(self.dirlink, self.dirlink_target)
