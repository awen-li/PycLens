# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_broken_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not os_helper.can_symlink():
        return self.skipTest('cannot create symbolic link')
    filename = self.create_file('file.txt')
    os.symlink(filename, os.path.join(self.path, 'symlink.txt'))
    entries = self.get_entries(['file.txt', 'symlink.txt'])
    entry = entries['symlink.txt']
    os.unlink(filename)
    self.assertGreater(entry.inode(), 0)
    self.assertFalse(entry.is_dir())
    self.assertFalse(entry.is_file())
    self.assertFalse(entry.is_dir(follow_symlinks=False))
    self.assertFalse(entry.is_file(follow_symlinks=False))
    self.assertTrue(entry.is_symlink())
    self.assertRaises(FileNotFoundError, entry.stat)
    entry.stat(follow_symlinks=False)
