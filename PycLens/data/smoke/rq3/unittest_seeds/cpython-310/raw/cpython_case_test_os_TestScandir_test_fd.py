# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn(os.scandir, os.supports_fd)
    self.create_file('file.txt')
    expected_names = ['file.txt']
    if os_helper.can_symlink():
        os.symlink('file.txt', os.path.join(self.path, 'link'))
        expected_names.append('link')
    with os_helper.open_dir_fd(self.path) as fd:
        with os.scandir(fd) as it:
            entries = list(it)
        names = [entry.name for entry in entries]
        self.assertEqual(sorted(names), expected_names)
        self.assertEqual(names, os.listdir(fd))
        for entry in entries:
            self.assertEqual(entry.path, entry.name)
            self.assertEqual(os.fspath(entry), entry.name)
            self.assertEqual(entry.is_symlink(), entry.name == 'link')
            if os.stat in os.supports_dir_fd:
                st = os.stat(entry.name, dir_fd=fd)
                self.assertEqual(entry.stat(), st)
                st = os.stat(entry.name, dir_fd=fd, follow_symlinks=False)
                self.assertEqual(entry.stat(follow_symlinks=False), st)
