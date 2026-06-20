# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: MakedirTests_test_exist_ok_existing_regular_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = os_helper.TESTFN
    path = os.path.join(os_helper.TESTFN, 'dir1')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('abc')
    self.assertRaises(OSError, os.makedirs, path)
    self.assertRaises(OSError, os.makedirs, path, exist_ok=False)
    self.assertRaises(OSError, os.makedirs, path, exist_ok=True)
    os.remove(path)
