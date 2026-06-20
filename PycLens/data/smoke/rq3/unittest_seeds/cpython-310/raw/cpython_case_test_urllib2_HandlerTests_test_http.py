# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    o = h.parent = MockOpener()
    url = 'http://example.com/'
    for (method, data) in [('GET', None), ('POST', b'blah')]:
        req = Request(url, data, {'Foo': 'bar'})
        req.timeout = None
        req.add_unredirected_header('Spam', 'eggs')
        http = MockHTTPClass()
        r = h.do_open(http, req)
        r.read
        r.readline
        r.info
        r.geturl
        (r.code, r.msg == 200, 'OK')
        hdrs = r.info()
        hdrs.get
        hdrs.__contains__
        self.assertEqual(r.geturl(), url)
        self.assertEqual(http.host, 'example.com')
        self.assertEqual(http.level, 0)
        self.assertEqual(http.method, method)
        self.assertEqual(http.selector, '/')
        self.assertEqual(http.req_headers, [('Connection', 'close'), ('Foo', 'bar'), ('Spam', 'eggs')])
        self.assertEqual(http.data, data)
    http.raise_on_endheaders = True
    self.assertRaises(urllib.error.URLError, h.do_open, http, req)
    req = Request('http://example.com/', 'badpost')
    self.assertRaises(TypeError, h.do_request_, req)
    o.addheaders = [('Spam', 'eggs')]
    for data in (b'', None):
        req = Request('http://example.com/', data)
        r = MockResponse(200, 'OK', {}, '')
        newreq = h.do_request_(req)
        if data is None:
            self.assertNotIn('Content-length', req.unredirected_hdrs)
            self.assertNotIn('Content-type', req.unredirected_hdrs)
        else:
            self.assertEqual(req.unredirected_hdrs['Content-length'], '0')
            self.assertEqual(req.unredirected_hdrs['Content-type'], 'application/x-www-form-urlencoded')
        self.assertEqual(req.unredirected_hdrs['Host'], 'example.com')
        self.assertEqual(req.unredirected_hdrs['Spam'], 'eggs')
        req.add_unredirected_header('Content-length', 'foo')
        req.add_unredirected_header('Content-type', 'bar')
        req.add_unredirected_header('Host', 'baz')
        req.add_unredirected_header('Spam', 'foo')
        newreq = h.do_request_(req)
        self.assertEqual(req.unredirected_hdrs['Content-length'], 'foo')
        self.assertEqual(req.unredirected_hdrs['Content-type'], 'bar')
        self.assertEqual(req.unredirected_hdrs['Host'], 'baz')
        self.assertEqual(req.unredirected_hdrs['Spam'], 'foo')
