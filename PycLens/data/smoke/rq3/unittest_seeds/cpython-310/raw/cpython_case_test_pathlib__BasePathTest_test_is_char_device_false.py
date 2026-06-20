# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_char_device_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertFalse((P / 'fileA').is_char_device())
    self.assertFalse((P / 'dirA').is_char_device())
    self.assertFalse((P / 'non-existing').is_char_device())
    self.assertFalse((P / 'fileA' / 'bah').is_char_device())
    self.assertIs((P / 'fileA\udfff').is_char_device(), False)
    self.assertIs((P / 'fileA\x00').is_char_device(), False)
