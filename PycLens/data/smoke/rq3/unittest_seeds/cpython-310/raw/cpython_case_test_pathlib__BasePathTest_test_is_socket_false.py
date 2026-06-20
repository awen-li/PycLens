# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_socket_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertFalse((P / 'fileA').is_socket())
    self.assertFalse((P / 'dirA').is_socket())
    self.assertFalse((P / 'non-existing').is_socket())
    self.assertFalse((P / 'fileA' / 'bah').is_socket())
    self.assertIs((P / 'fileA\udfff').is_socket(), False)
    self.assertIs((P / 'fileA\x00').is_socket(), False)
