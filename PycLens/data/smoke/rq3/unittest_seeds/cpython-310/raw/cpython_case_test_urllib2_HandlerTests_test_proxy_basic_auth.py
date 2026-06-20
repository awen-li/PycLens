# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_proxy_basic_auth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opener = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(http='proxy.example.com:3128'))
    opener.add_handler(ph)
    password_manager = MockPasswordManager()
    auth_handler = urllib.request.ProxyBasicAuthHandler(password_manager)
    realm = 'ACME Networks'
    http_handler = MockHTTPHandler(407, 'Proxy-Authenticate: Basic realm="%s"\r\n\r\n' % realm)
    opener.add_handler(auth_handler)
    opener.add_handler(http_handler)
    self._test_basic_auth(opener, auth_handler, 'Proxy-authorization', realm, http_handler, password_manager, 'http://acme.example.com:3128/protected', 'proxy.example.com:3128')
