# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_redirect_no_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(urllib.request.urlcleanup)
    real_class = http.client.HTTPConnection
    response1 = b'HTTP/1.1 302 Found\r\nLocation: ?query\r\n\r\n'
    http.client.HTTPConnection = test_urllib.fakehttp(response1)
    self.addCleanup(setattr, http.client, 'HTTPConnection', real_class)
    urls = iter(('/path', '/path?query'))

    def request(conn, method, url, *pos, **kw):
        self.assertEqual(url, next(urls))
        real_class.request(conn, method, url, *pos, **kw)
        conn.__class__.fakedata = b'HTTP/1.1 200 OK\r\n\r\nHello!'
    http.client.HTTPConnection.request = request
    fp = urllib.request.urlopen('http://python.org/path')
    self.assertEqual(fp.geturl(), 'http://python.org/path?query')
