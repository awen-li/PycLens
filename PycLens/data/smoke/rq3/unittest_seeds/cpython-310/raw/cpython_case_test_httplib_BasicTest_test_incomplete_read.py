# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_incomplete_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\nHello\r\n')
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    try:
        resp.read()
    except client.IncompleteRead as i:
        self.assertEqual(i.partial, b'Hello\r\n')
        self.assertEqual(repr(i), 'IncompleteRead(7 bytes read, 3 more expected)')
        self.assertEqual(str(i), 'IncompleteRead(7 bytes read, 3 more expected)')
        self.assertTrue(resp.isclosed())
    else:
        self.fail('IncompleteRead expected')
