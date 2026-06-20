# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (transfer, data) in (('Connection: close', b'data'), ('Transfer-Encoding: chunked', b'4\r\ndata\r\n0\r\n\r\n'), ('Content-Length: 4', b'data')):
        header = 'HTTP/1.1 200 OK\r\n{}\r\n\r\n'.format(transfer)
        conn = test_urllib.fakehttp(header.encode() + data)
        handler = urllib.request.AbstractHTTPHandler()
        req = Request('http://dummy/')
        req.timeout = None
        with handler.do_open(conn, req) as resp:
            resp.read()
        self.assertTrue(conn.fakesock.closed, 'Connection not closed with {!r}'.format(transfer))
