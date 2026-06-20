# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: ProxyAuthTests_test_proxy_qop_auth_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.proxy_digest_handler.add_password(self.REALM, self.URL, self.USER, self.PASSWD)
    self.digest_auth_handler.set_qop('auth')
    with self.opener.open(self.URL) as result:
        while result.read():
            pass
