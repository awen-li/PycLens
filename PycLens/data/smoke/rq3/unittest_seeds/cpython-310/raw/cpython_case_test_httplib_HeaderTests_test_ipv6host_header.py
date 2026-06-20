# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_ipv6host_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'GET /foo HTTP/1.1\r\nHost: [2001::]:81\r\nAccept-Encoding: identity\r\n\r\n'
    conn = client.HTTPConnection('[2001::]:81')
    sock = FakeSocket('')
    conn.sock = sock
    conn.request('GET', '/foo')
    self.assertTrue(sock.data.startswith(expected))
    expected = b'GET /foo HTTP/1.1\r\nHost: [2001:102A::]\r\nAccept-Encoding: identity\r\n\r\n'
    conn = client.HTTPConnection('[2001:102A::]')
    sock = FakeSocket('')
    conn.sock = sock
    conn.request('GET', '/foo')
    self.assertTrue(sock.data.startswith(expected))
