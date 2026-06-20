# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_large_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.get_file_system(self.dirname) != 'NTFS':
        self.skipTest('requires NTFS')
    large = 5000000000
    os.utime(self.fname, (large, large))
    self.assertEqual(os.stat(self.fname).st_mtime, large)
