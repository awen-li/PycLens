# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_device_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    b = self.BytesIO()
    b.fileno = lambda : _testcapi.INT_MAX + 1
    self.assertRaises(OverflowError, self.TextIOWrapper, b, encoding='locale')
    b.fileno = lambda : _testcapi.UINT_MAX + 1
    self.assertRaises(OverflowError, self.TextIOWrapper, b, encoding='locale')
