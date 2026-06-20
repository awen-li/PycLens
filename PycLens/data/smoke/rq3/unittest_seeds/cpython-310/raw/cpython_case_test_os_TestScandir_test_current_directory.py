# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_current_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = self.create_file()
    old_dir = os.getcwd()
    try:
        os.chdir(self.path)
        entries = dict(((entry.name, entry) for entry in os.scandir()))
        self.assertEqual(sorted(entries.keys()), [os.path.basename(filename)])
    finally:
        os.chdir(old_dir)
