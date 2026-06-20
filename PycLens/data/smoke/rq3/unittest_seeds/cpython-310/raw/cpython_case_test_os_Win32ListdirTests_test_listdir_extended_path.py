# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32ListdirTests_test_listdir_extended_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = '\\\\?\\' + os.path.abspath(os_helper.TESTFN)
    self.assertEqual(sorted(os.listdir(path)), self.created_paths)
    path = b'\\\\?\\' + os.fsencode(os.path.abspath(os_helper.TESTFN))
    self.assertEqual(sorted(os.listdir(path)), [os.fsencode(path) for path in self.created_paths])
