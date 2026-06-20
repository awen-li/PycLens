# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_fifo_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertFalse((P / 'fileA').is_fifo())
    self.assertFalse((P / 'dirA').is_fifo())
    self.assertFalse((P / 'non-existing').is_fifo())
    self.assertFalse((P / 'fileA' / 'bah').is_fifo())
    self.assertIs((P / 'fileA\udfff').is_fifo(), False)
    self.assertIs((P / 'fileA\x00').is_fifo(), False)
