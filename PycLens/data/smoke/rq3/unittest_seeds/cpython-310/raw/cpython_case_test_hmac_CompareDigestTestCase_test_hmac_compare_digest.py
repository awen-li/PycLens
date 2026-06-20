# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: CompareDigestTestCase_test_hmac_compare_digest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_compare_digest(hmac.compare_digest)
    if openssl_compare_digest is not None:
        self.assertIs(hmac.compare_digest, openssl_compare_digest)
    else:
        self.assertIs(hmac.compare_digest, operator_compare_digest)
