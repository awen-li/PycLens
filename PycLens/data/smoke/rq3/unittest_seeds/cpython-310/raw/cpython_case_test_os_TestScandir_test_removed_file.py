# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_removed_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entry = self.create_file_entry()
    os.unlink(entry.path)
    self.assertFalse(entry.is_dir())
    if os.name == 'nt':
        self.assertTrue(entry.is_file())
    self.assertFalse(entry.is_symlink())
    if os.name == 'nt':
        self.assertRaises(FileNotFoundError, entry.inode)
        entry.stat()
        entry.stat(follow_symlinks=False)
    else:
        self.assertGreater(entry.inode(), 0)
        self.assertRaises(FileNotFoundError, entry.stat)
        self.assertRaises(FileNotFoundError, entry.stat, follow_symlinks=False)
