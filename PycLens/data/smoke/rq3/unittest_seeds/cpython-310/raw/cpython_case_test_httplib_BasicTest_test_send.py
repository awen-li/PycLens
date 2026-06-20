# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'this is a test this is only a test'
    conn = client.HTTPConnection('example.com')
    sock = FakeSocket(None)
    conn.sock = sock
    conn.send(expected)
    self.assertEqual(expected, sock.data)
    sock.data = b''
    conn.send(array.array('b', expected))
    self.assertEqual(expected, sock.data)
    sock.data = b''
    conn.send(io.BytesIO(expected))
    self.assertEqual(expected, sock.data)
