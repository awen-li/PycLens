# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: KDFTests_test_pbkdf2_hmac_py

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings():
        self._test_pbkdf2_hmac(builtin_hashlib.pbkdf2_hmac, builtin_hashes)
