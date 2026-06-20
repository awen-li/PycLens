# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(binascii.Error, Exception))
    self.assertTrue(issubclass(binascii.Incomplete, Exception))
