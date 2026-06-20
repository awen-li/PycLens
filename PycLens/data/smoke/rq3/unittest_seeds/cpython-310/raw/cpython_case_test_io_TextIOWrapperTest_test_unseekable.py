# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_unseekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.MockUnseekableIO(self.testdata), encoding='utf-8')
    self.assertRaises(self.UnsupportedOperation, txt.tell)
    self.assertRaises(self.UnsupportedOperation, txt.seek, 0)
