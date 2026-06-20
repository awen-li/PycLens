# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertTrue((P / 'dirA').is_dir())
    self.assertFalse((P / 'fileA').is_dir())
    self.assertFalse((P / 'non-existing').is_dir())
    self.assertFalse((P / 'fileA' / 'bah').is_dir())
    if os_helper.can_symlink():
        self.assertFalse((P / 'linkA').is_dir())
        self.assertTrue((P / 'linkB').is_dir())
        self.assertFalse((P / 'brokenLink').is_dir(), False)
    self.assertIs((P / 'dirA\udfff').is_dir(), False)
    self.assertIs((P / 'dirA\x00').is_dir(), False)
