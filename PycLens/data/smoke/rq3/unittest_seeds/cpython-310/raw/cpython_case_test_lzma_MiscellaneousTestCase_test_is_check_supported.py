# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: MiscellaneousTestCase_test_is_check_supported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(lzma.is_check_supported(lzma.CHECK_NONE))
    self.assertTrue(lzma.is_check_supported(lzma.CHECK_CRC32))
    self.assertFalse(lzma.is_check_supported(lzma.CHECK_ID_MAX + 1))
    self.assertFalse(lzma.is_check_supported(lzma.CHECK_UNKNOWN))
