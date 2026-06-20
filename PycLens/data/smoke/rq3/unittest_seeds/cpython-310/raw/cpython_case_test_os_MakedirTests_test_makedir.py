# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MakedirTests_test_makedir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = os_helper.TESTFN
    path = os.path.join(base, 'dir1', 'dir2', 'dir3')
    os.makedirs(path)
    path = os.path.join(base, 'dir1', 'dir2', 'dir3', 'dir4')
    os.makedirs(path)
    self.assertRaises(OSError, os.makedirs, os.curdir)
    path = os.path.join(base, 'dir1', 'dir2', 'dir3', 'dir4', 'dir5', os.curdir)
    os.makedirs(path)
    path = os.path.join(base, 'dir1', os.curdir, 'dir2', 'dir3', 'dir4', 'dir5', 'dir6')
    os.makedirs(path)
