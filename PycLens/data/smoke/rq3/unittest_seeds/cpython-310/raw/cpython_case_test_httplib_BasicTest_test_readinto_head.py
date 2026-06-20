# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_readinto_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: 14432\r\n\r\n', NoEOFBytesIO)
    resp = client.HTTPResponse(sock, method='HEAD')
    resp.begin()
    b = bytearray(5)
    if resp.readinto(b) != 0:
        self.fail('Did not expect response from HEAD request')
    self.assertEqual(bytes(b), b'\x00' * 5)
