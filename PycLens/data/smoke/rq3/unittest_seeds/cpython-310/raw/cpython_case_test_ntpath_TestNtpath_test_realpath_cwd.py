# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    os_helper.unlink(ABSTFN)
    os_helper.rmtree(ABSTFN)
    os.mkdir(ABSTFN)
    self.addCleanup(os_helper.rmtree, ABSTFN)
    test_dir_long = ntpath.join(ABSTFN, 'MyVeryLongDirectoryName')
    os.mkdir(test_dir_long)
    test_dir_short = _getshortpathname(test_dir_long)
    test_file_long = ntpath.join(test_dir_long, 'file.txt')
    test_file_short = ntpath.join(test_dir_short, 'file.txt')
    with open(test_file_long, 'wb') as f:
        f.write(b'content')
    self.assertPathEqual(test_file_long, ntpath.realpath(test_file_short))
    with os_helper.change_cwd(test_dir_long):
        self.assertPathEqual(test_file_long, ntpath.realpath('file.txt'))
    with os_helper.change_cwd(test_dir_long.lower()):
        self.assertPathEqual(test_file_long, ntpath.realpath('file.txt'))
    with os_helper.change_cwd(test_dir_short):
        self.assertPathEqual(test_file_long, ntpath.realpath('file.txt'))
