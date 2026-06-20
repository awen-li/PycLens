# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_overflowing_chunked_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n' + '0' * 65536 + 'a\r\nhello world\r\n0\r\n\r\n'
    resp = client.HTTPResponse(FakeSocket(body))
    resp.begin()
    self.assertRaises(client.LineTooLong, resp.read)
