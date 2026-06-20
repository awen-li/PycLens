# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ExceptionTestCase_test_disallow_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.check_disallow_instantiation(self, type(zlib.compressobj()))
    support.check_disallow_instantiation(self, type(zlib.decompressobj()))
