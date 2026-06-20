# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls('a/b/c')
    self.assertEqual(str(p), 'a\\b\\c')
    p = self.cls('c:/a/b/c')
    self.assertEqual(str(p), 'c:\\a\\b\\c')
    p = self.cls('//a/b')
    self.assertEqual(str(p), '\\\\a\\b\\')
    p = self.cls('//a/b/c')
    self.assertEqual(str(p), '\\\\a\\b\\c')
    p = self.cls('//a/b/c/d')
    self.assertEqual(str(p), '\\\\a\\b\\c\\d')
