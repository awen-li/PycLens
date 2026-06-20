# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from_url = 'http://example.com/a.html'
    to_url = 'http://example.com/b.html'
    h = urllib.request.HTTPRedirectHandler()
    o = h.parent = MockOpener()
    for code in (301, 302, 303, 307):
        for data in (None, 'blah\nblah\n'):
            method = getattr(h, 'http_error_%s' % code)
            req = Request(from_url, data)
            req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT
            req.add_header('Nonsense', 'viking=withhold')
            if data is not None:
                req.add_header('Content-Length', str(len(data)))
            req.add_unredirected_header('Spam', 'spam')
            try:
                method(req, MockFile(), code, 'Blah', MockHeaders({'location': to_url}))
            except urllib.error.HTTPError:
                self.assertEqual(code, 307)
                self.assertIsNotNone(data)
            self.assertEqual(o.req.get_full_url(), to_url)
            try:
                self.assertEqual(o.req.get_method(), 'GET')
            except AttributeError:
                self.assertFalse(o.req.data)
            headers = [x.lower() for x in o.req.headers]
            self.assertNotIn('content-length', headers)
            self.assertNotIn('content-type', headers)
            self.assertEqual(o.req.headers['Nonsense'], 'viking=withhold')
            self.assertNotIn('Spam', o.req.headers)
            self.assertNotIn('Spam', o.req.unredirected_hdrs)
    req = Request(from_url)
    req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT

    def redirect(h, req, url=to_url):
        h.http_error_302(req, MockFile(), 302, 'Blah', MockHeaders({'location': url}))
    req = Request(from_url, origin_req_host='example.com')
    count = 0
    req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT
    try:
        while 1:
            redirect(h, req, 'http://example.com/')
            count = count + 1
    except urllib.error.HTTPError:
        self.assertEqual(count, urllib.request.HTTPRedirectHandler.max_repeats)
    req = Request(from_url, origin_req_host='example.com')
    count = 0
    req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT
    try:
        while 1:
            redirect(h, req, 'http://example.com/%d' % count)
            count = count + 1
    except urllib.error.HTTPError:
        self.assertEqual(count, urllib.request.HTTPRedirectHandler.max_redirections)
