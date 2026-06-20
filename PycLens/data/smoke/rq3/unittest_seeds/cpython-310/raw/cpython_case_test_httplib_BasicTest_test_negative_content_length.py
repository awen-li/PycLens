# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_negative_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: -1\r\n\r\nHello\r\n')
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    self.assertEqual(resp.read(), b'Hello\r\n')
    self.assertTrue(resp.isclosed())
