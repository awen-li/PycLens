# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_12084

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    level1 = os.path.abspath(os_helper.TESTFN)
    level2 = os.path.join(level1, 'level2')
    level3 = os.path.join(level2, 'level3')
    self.addCleanup(os_helper.rmtree, level1)
    os.mkdir(level1)
    os.mkdir(level2)
    os.mkdir(level3)
    file1 = os.path.abspath(os.path.join(level1, 'file1'))
    create_file(file1)
    orig_dir = os.getcwd()
    try:
        os.chdir(level2)
        link = os.path.join(level2, 'link')
        os.symlink(os.path.relpath(file1), 'link')
        self.assertIn('link', os.listdir(os.getcwd()))
        self.assertEqual(os.stat(file1), os.stat('link'))
        os.chdir(level1)
        self.assertEqual(os.stat(file1), os.stat(os.path.relpath(link)))
        os.chdir(level3)
        self.assertEqual(os.stat(file1), os.stat(os.path.relpath(link)))
    finally:
        os.chdir(orig_dir)
