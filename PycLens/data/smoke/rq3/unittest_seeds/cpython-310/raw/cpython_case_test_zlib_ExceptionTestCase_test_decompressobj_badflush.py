# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ExceptionTestCase_test_decompressobj_badflush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, zlib.decompressobj().flush, 0)
    self.assertRaises(ValueError, zlib.decompressobj().flush, -1)
