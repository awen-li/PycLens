# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarUnicodeTest_test_unicode_name2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_ustar_name('0123456789' * 9 + '012345ÿÿ')
    self._test_ustar_name('0123456789' * 9 + '0123456ÿÿ', ValueError)
