# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_basic_and_digest_auth_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RecordingOpenerDirector(OpenerDirector):

        def __init__(self):
            OpenerDirector.__init__(self)
            self.recorded = []

        def record(self, info):
            self.recorded.append(info)

    class TestDigestAuthHandler(urllib.request.HTTPDigestAuthHandler):

        def http_error_401(self, *args, **kwds):
            self.parent.record('digest')
            urllib.request.HTTPDigestAuthHandler.http_error_401(self, *args, **kwds)

    class TestBasicAuthHandler(urllib.request.HTTPBasicAuthHandler):

        def http_error_401(self, *args, **kwds):
            self.parent.record('basic')
            urllib.request.HTTPBasicAuthHandler.http_error_401(self, *args, **kwds)
    opener = RecordingOpenerDirector()
    password_manager = MockPasswordManager()
    digest_handler = TestDigestAuthHandler(password_manager)
    basic_handler = TestBasicAuthHandler(password_manager)
    realm = 'ACME Networks'
    http_handler = MockHTTPHandler(401, 'WWW-Authenticate: Basic realm="%s"\r\n\r\n' % realm)
    opener.add_handler(basic_handler)
    opener.add_handler(digest_handler)
    opener.add_handler(http_handler)
    self._test_basic_auth(opener, basic_handler, 'Authorization', realm, http_handler, password_manager, 'http://acme.example.com/protected', 'http://acme.example.com/protected')
    self.assertEqual(opener.recorded, ['digest', 'basic'] * 2)
