# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_basic_prior_auth_auto_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (user, password) = ('wile', 'coyote')
    request_url = 'http://acme.example.com/protected'
    http_handler = MockHTTPHandlerCheckAuth(200)
    pwd_manager = HTTPPasswordMgrWithPriorAuth()
    auth_prior_handler = HTTPBasicAuthHandler(pwd_manager)
    auth_prior_handler.add_password(None, request_url, user, password, is_authenticated=True)
    self.assertTrue(pwd_manager.is_authenticated(request_url))
    self.assertTrue(pwd_manager.is_authenticated(request_url + '/nested'))
    self.assertFalse(pwd_manager.is_authenticated(request_url + 'plain'))
    opener = OpenerDirector()
    opener.add_handler(auth_prior_handler)
    opener.add_handler(http_handler)
    opener.open(request_url)
    self.assertTrue(http_handler.has_auth_header)
