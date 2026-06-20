# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_non_matching_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.chmod(self.temp_file.name, stat.S_IREAD)
    if os.access(self.temp_file.name, os.W_OK):
        self.skipTest("can't set the file read-only")
    rv = shutil.which(self.file, path=self.dir, mode=os.W_OK)
    self.assertIsNone(rv)
