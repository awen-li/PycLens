# Source Generated with Decompyle++
# File: cpython-38-3161b78f9aee.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.read(), b'')
    self.assertTrue(resp.isclosed())
    self.assertFalse(resp.closed)
    resp.close()
    self.assertTrue(resp.closed)

if __name__ == '__main__':
    __pybcsec_seed__()
# WARNING: Decompyle incomplete
