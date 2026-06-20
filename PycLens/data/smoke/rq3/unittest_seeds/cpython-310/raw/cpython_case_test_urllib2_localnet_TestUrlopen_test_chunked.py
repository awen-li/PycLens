# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_chunked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_response = b'hello world'
    chunked_start = b'a\r\nhello worl\r\n1\r\nd\r\n0\r\n'
    response = [(200, [('Transfer-Encoding', 'chunked')], chunked_start)]
    handler = self.start_server(response)
    data = self.urlopen('http://localhost:%s/' % handler.port)
    self.assertEqual(data, expected_response)
