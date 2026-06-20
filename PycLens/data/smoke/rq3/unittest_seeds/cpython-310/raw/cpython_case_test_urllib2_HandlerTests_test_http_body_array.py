# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_body_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    o = h.parent = MockOpener()
    iterable_array = array.array('I', [1, 2, 3, 4])
    for headers in ({}, {'Content-Length': 16}):
        req = Request('http://example.com/', iterable_array, headers)
        newreq = h.do_request_(req)
        self.assertEqual(int(newreq.get_header('Content-length')), 16)
