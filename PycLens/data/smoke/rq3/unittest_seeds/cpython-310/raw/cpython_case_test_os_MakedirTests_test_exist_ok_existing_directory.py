# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MakedirTests_test_exist_ok_existing_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(os_helper.TESTFN, 'dir1')
    mode = 511
    old_mask = os.umask(18)
    os.makedirs(path, mode)
    self.assertRaises(OSError, os.makedirs, path, mode)
    self.assertRaises(OSError, os.makedirs, path, mode, exist_ok=False)
    os.makedirs(path, 510, exist_ok=True)
    os.makedirs(path, mode=mode, exist_ok=True)
    os.umask(old_mask)
    os.makedirs(os.path.abspath('/'), exist_ok=True)
