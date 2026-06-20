# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_mount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    R = self.cls('/')
    self.assertFalse((P / 'fileA').is_mount())
    self.assertFalse((P / 'dirA').is_mount())
    self.assertFalse((P / 'non-existing').is_mount())
    self.assertFalse((P / 'fileA' / 'bah').is_mount())
    self.assertTrue(R.is_mount())
    if os_helper.can_symlink():
        self.assertFalse((P / 'linkA').is_mount())
    self.assertIs(self.cls('/\udfff').is_mount(), False)
    self.assertIs(self.cls('/\x00').is_mount(), False)
