# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_body_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    o = h.parent = MockOpener()

    def iterable_body():
        yield b'one'
    for headers in ({}, {'Content-Length': 11}):
        req = Request('http://example.com/', iterable_body(), headers)
        newreq = h.do_request_(req)
        if not headers:
            self.assertEqual(newreq.get_header('Content-length'), None)
            self.assertEqual(newreq.get_header('Transfer-encoding'), 'chunked')
        else:
            self.assertEqual(int(newreq.get_header('Content-length')), 11)
