# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MakedirTests_test_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_umask(2):
        base = os_helper.TESTFN
        parent = os.path.join(base, 'dir1')
        path = os.path.join(parent, 'dir2')
        os.makedirs(path, 365)
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isdir(path))
        if os.name != 'nt':
            self.assertEqual(os.stat(path).st_mode & 511, 365)
            self.assertEqual(os.stat(parent).st_mode & 511, 509)
