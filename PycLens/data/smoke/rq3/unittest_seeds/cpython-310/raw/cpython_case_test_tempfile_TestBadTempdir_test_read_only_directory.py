# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestBadTempdir_test_read_only_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with _inside_empty_temp_dir():
        oldmode = mode = os.stat(tempfile.tempdir).st_mode
        mode &= ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
        os.chmod(tempfile.tempdir, mode)
        try:
            if os.access(tempfile.tempdir, os.W_OK):
                self.skipTest("can't set the directory read-only")
            with self.assertRaises(PermissionError):
                self.make_temp()
            self.assertEqual(os.listdir(tempfile.tempdir), [])
        finally:
            os.chmod(tempfile.tempdir, oldmode)
