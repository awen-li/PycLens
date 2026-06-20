# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertFalse((P / 'fileA').is_symlink())
    self.assertFalse((P / 'dirA').is_symlink())
    self.assertFalse((P / 'non-existing').is_symlink())
    self.assertFalse((P / 'fileA' / 'bah').is_symlink())
    if os_helper.can_symlink():
        self.assertTrue((P / 'linkA').is_symlink())
        self.assertTrue((P / 'linkB').is_symlink())
        self.assertTrue((P / 'brokenLink').is_symlink())
    self.assertIs((P / 'fileA\udfff').is_file(), False)
    self.assertIs((P / 'fileA\x00').is_file(), False)
    if os_helper.can_symlink():
        self.assertIs((P / 'linkA\udfff').is_file(), False)
        self.assertIs((P / 'linkA\x00').is_file(), False)
