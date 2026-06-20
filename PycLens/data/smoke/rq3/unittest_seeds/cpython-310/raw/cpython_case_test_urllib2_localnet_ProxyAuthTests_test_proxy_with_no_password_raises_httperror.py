# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: ProxyAuthTests_test_proxy_with_no_password_raises_httperror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.digest_auth_handler.set_qop('auth')
    self.assertRaises(urllib.error.HTTPError, self.opener.open, self.URL)
