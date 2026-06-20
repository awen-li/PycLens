# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_ismount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(ntpath.ismount('c:\\'))
    self.assertTrue(ntpath.ismount('C:\\'))
    self.assertTrue(ntpath.ismount('c:/'))
    self.assertTrue(ntpath.ismount('C:/'))
    self.assertTrue(ntpath.ismount('\\\\.\\c:\\'))
    self.assertTrue(ntpath.ismount('\\\\.\\C:\\'))
    self.assertTrue(ntpath.ismount(b'c:\\'))
    self.assertTrue(ntpath.ismount(b'C:\\'))
    self.assertTrue(ntpath.ismount(b'c:/'))
    self.assertTrue(ntpath.ismount(b'C:/'))
    self.assertTrue(ntpath.ismount(b'\\\\.\\c:\\'))
    self.assertTrue(ntpath.ismount(b'\\\\.\\C:\\'))
    with os_helper.temp_dir() as d:
        self.assertFalse(ntpath.ismount(d))
    if sys.platform == 'win32':
        (drive, path) = ntpath.splitdrive(sys.executable)
        with os_helper.change_cwd(ntpath.dirname(sys.executable)):
            self.assertFalse(ntpath.ismount(drive.lower()))
            self.assertFalse(ntpath.ismount(drive.upper()))
        self.assertTrue(ntpath.ismount('\\\\localhost\\c$'))
        self.assertTrue(ntpath.ismount('\\\\localhost\\c$\\'))
        self.assertTrue(ntpath.ismount(b'\\\\localhost\\c$'))
        self.assertTrue(ntpath.ismount(b'\\\\localhost\\c$\\'))
