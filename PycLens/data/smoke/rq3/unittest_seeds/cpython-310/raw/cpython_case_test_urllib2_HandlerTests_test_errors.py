# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.HTTPErrorProcessor()
    o = h.parent = MockOpener()
    url = 'http://example.com/'
    req = Request(url)
    r = MockResponse(200, 'OK', {}, '', url)
    newr = h.http_response(req, r)
    self.assertIs(r, newr)
    self.assertFalse(hasattr(o, 'proto'))
    r = MockResponse(202, 'Accepted', {}, '', url)
    newr = h.http_response(req, r)
    self.assertIs(r, newr)
    self.assertFalse(hasattr(o, 'proto'))
    r = MockResponse(206, 'Partial content', {}, '', url)
    newr = h.http_response(req, r)
    self.assertIs(r, newr)
    self.assertFalse(hasattr(o, 'proto'))
    r = MockResponse(502, 'Bad gateway', {}, '', url)
    self.assertIsNone(h.http_response(req, r))
    self.assertEqual(o.proto, 'http')
    self.assertEqual(o.args, (req, r, 502, 'Bad gateway', {}))
