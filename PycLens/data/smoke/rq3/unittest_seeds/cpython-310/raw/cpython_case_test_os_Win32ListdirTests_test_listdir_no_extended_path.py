# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32ListdirTests_test_listdir_no_extended_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(sorted(os.listdir(os_helper.TESTFN)), self.created_paths)
    self.assertEqual(sorted(os.listdir(os.fsencode(os_helper.TESTFN))), [os.fsencode(path) for path in self.created_paths])
