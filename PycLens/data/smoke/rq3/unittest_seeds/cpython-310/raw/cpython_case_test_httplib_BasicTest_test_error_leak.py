# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_error_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    response = None

    class Response(client.HTTPResponse):

        def __init__(self, *pos, **kw):
            nonlocal response
            response = self
            client.HTTPResponse.__init__(self, *pos, **kw)
    conn.response_class = Response
    conn.sock = FakeSocket('Invalid status line')
    conn.request('GET', '/')
    self.assertRaises(client.BadStatusLine, conn.getresponse)
    self.assertTrue(response.closed)
    self.assertTrue(conn.sock.file_closed)
