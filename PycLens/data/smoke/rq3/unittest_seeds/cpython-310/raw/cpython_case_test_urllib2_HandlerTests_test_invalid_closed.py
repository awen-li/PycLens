# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_invalid_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = test_urllib.fakehttp(b'')
    handler = urllib.request.AbstractHTTPHandler()
    req = Request('http://dummy/')
    req.timeout = None
    with self.assertRaises(http.client.BadStatusLine):
        handler.do_open(conn, req)
    self.assertTrue(conn.fakesock.closed, 'Connection not closed')
