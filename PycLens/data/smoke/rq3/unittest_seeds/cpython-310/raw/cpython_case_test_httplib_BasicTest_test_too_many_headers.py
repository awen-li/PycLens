# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_too_many_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    headers = '\r\n'.join(('Header%d: foo' % i for i in range(client._MAXHEADERS + 1))) + '\r\n'
    text = 'HTTP/1.1 200 OK\r\n' + headers
    s = FakeSocket(text)
    r = client.HTTPResponse(s)
    self.assertRaisesRegex(client.HTTPException, 'got more than \\d+ headers', r.begin)
