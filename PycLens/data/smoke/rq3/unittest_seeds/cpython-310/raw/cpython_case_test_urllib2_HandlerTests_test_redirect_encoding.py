# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_redirect_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Handler(urllib.request.HTTPHandler):

        def http_open(self, req):
            result = self.do_open(self.connection, req)
            self.last_buf = self.connection.buf
            self.connection = test_urllib.fakehttp(b'HTTP/1.1 200 OK\r\nContent-Length: 3\r\n\r\n123')
            return result
    handler = Handler()
    opener = urllib.request.build_opener(handler)
    tests = ((b'/p\xc3\xa5-dansk/', b'/p%C3%A5-dansk/'), (b'/spaced%20path/', b'/spaced%20path/'), (b'/spaced path/', b'/spaced%20path/'), (b'/?p\xc3\xa5-dansk', b'/?p%C3%A5-dansk'))
    for [location, result] in tests:
        with self.subTest(repr(location)):
            handler.connection = test_urllib.fakehttp(b'HTTP/1.1 302 Redirect\r\nLocation: ' + location + b'\r\n\r\n')
            response = opener.open('http://example.com/')
            expected = b'GET ' + result + b' '
            request = handler.last_buf
            self.assertTrue(request.startswith(expected), repr(request))
