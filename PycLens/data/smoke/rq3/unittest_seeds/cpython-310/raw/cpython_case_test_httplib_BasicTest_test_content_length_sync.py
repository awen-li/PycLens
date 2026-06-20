# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_content_length_sync

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extradata = b'extradata'
    expected = b'Hello123\r\n'
    sock = FakeSocket(b'HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\n' + expected + extradata)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    self.assertEqual(resp.read(), expected)
    self.assertEqual(sock.file.read(), extradata)
    resp.close()
