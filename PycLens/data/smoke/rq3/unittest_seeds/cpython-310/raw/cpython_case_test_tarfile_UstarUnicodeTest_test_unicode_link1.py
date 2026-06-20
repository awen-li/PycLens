# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarUnicodeTest_test_unicode_link1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_ustar_link('0123456789' * 10)
    self._test_ustar_link('0123456789' * 10 + '0', ValueError)
    self._test_ustar_link('0123456789' * 9 + '01234567ÿ')
    self._test_ustar_link('0123456789' * 9 + '012345678ÿ', ValueError)
