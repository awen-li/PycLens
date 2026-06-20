# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_file_link

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.symlink(self.filelink_target, self.filelink)
    self.assertTrue(os.path.exists(self.filelink))
    self.assertTrue(os.path.isfile(self.filelink))
    self.assertTrue(os.path.islink(self.filelink))
    self.check_stat(self.filelink, self.filelink_target)
