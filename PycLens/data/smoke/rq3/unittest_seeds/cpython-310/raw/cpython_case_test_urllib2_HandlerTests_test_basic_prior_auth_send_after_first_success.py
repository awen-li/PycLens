# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_basic_prior_auth_send_after_first_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (user, password) = ('wile', 'coyote')
    request_url = 'http://acme.example.com/protected'
    realm = 'ACME'
    pwd_manager = HTTPPasswordMgrWithPriorAuth()
    auth_prior_handler = HTTPBasicAuthHandler(pwd_manager)
    auth_prior_handler.add_password(realm, request_url, user, password)
    is_auth = pwd_manager.is_authenticated(request_url)
    self.assertFalse(is_auth)
    opener = OpenerDirector()
    opener.add_handler(auth_prior_handler)
    http_handler = MockHTTPHandler(401, 'WWW-Authenticate: Basic realm="%s"\r\n\r\n' % None)
    opener.add_handler(http_handler)
    opener.open(request_url)
    is_auth = pwd_manager.is_authenticated(request_url)
    self.assertTrue(is_auth)
    http_handler = MockHTTPHandlerCheckAuth(200)
    self.assertFalse(http_handler.has_auth_header)
    opener = OpenerDirector()
    opener.add_handler(auth_prior_handler)
    opener.add_handler(http_handler)
    opener.open(request_url)
    self.assertTrue(http_handler.has_auth_header)
