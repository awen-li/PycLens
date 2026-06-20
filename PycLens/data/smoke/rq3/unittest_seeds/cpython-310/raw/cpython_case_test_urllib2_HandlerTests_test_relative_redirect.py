# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_relative_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from_url = 'http://example.com/a.html'
    relative_url = '/b.html'
    h = urllib.request.HTTPRedirectHandler()
    o = h.parent = MockOpener()
    req = Request(from_url)
    req.timeout = socket._GLOBAL_DEFAULT_TIMEOUT
    valid_url = urllib.parse.urljoin(from_url, relative_url)
    h.http_error_302(req, MockFile(), 302, "That's fine", MockHeaders({'location': valid_url}))
    self.assertEqual(o.req.get_full_url(), valid_url)
