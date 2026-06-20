# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_body_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    o = h.parent = MockOpener()
    file_obj = io.BytesIO()
    req = Request('http://example.com/', file_obj, {})
    newreq = h.do_request_(req)
    self.assertEqual(newreq.get_header('Transfer-encoding'), 'chunked')
    self.assertFalse(newreq.has_header('Content-length'))
    headers = {'Content-Length': 30}
    req = Request('http://example.com/', file_obj, headers)
    newreq = h.do_request_(req)
    self.assertEqual(int(newreq.get_header('Content-length')), 30)
    self.assertFalse(newreq.has_header('Transfer-encoding'))
    file_obj.close()
