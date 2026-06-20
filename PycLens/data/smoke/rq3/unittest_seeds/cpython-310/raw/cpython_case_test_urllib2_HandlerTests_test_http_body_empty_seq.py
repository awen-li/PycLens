# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_body_empty_seq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    h.parent = MockOpener()
    req = h.do_request_(Request('http://example.com/', ()))
    self.assertEqual(req.get_header('Transfer-encoding'), 'chunked')
    self.assertFalse(req.has_header('Content-length'))
