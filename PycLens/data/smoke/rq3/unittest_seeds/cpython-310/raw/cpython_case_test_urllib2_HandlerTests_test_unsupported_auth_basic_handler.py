# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_unsupported_auth_basic_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opener = OpenerDirector()
    basic_auth_handler = urllib.request.HTTPBasicAuthHandler(None)
    http_handler = MockHTTPHandler(401, 'WWW-Authenticate: NTLM\r\n\r\n')
    opener.add_handler(basic_auth_handler)
    opener.add_handler(http_handler)
    self.assertRaises(ValueError, opener.open, 'http://www.example.com')
