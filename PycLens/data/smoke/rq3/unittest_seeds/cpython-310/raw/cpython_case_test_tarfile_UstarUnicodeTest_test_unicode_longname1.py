# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarUnicodeTest_test_unicode_longname1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_ustar_name('0123456789' * 15 + '01234/' + '0123456789' * 10)
    self._test_ustar_name('0123456789' * 15 + '0123/4' + '0123456789' * 10, ValueError)
    self._test_ustar_name('0123456789' * 15 + '012ÿ/' + '0123456789' * 10)
    self._test_ustar_name('0123456789' * 15 + '0123ÿ/' + '0123456789' * 10, ValueError)
