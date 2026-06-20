# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_rename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os_helper.TESTFN
    old = sys.getrefcount(path)
    self.assertRaises(TypeError, os.rename, path, 0)
    new = sys.getrefcount(path)
    self.assertEqual(old, new)
