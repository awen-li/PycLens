# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertTrue((P / 'fileA').is_file())
    self.assertFalse((P / 'dirA').is_file())
    self.assertFalse((P / 'non-existing').is_file())
    self.assertFalse((P / 'fileA' / 'bah').is_file())
    if os_helper.can_symlink():
        self.assertTrue((P / 'linkA').is_file())
        self.assertFalse((P / 'linkB').is_file())
        self.assertFalse((P / 'brokenLink').is_file())
    self.assertIs((P / 'fileA\udfff').is_file(), False)
    self.assertIs((P / 'fileA\x00').is_file(), False)
