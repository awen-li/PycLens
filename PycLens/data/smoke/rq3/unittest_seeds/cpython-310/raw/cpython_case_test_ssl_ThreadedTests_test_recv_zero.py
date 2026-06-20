# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_recv_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = ThreadedEchoServer(CERTFILE)
    server.__enter__()
    self.addCleanup(server.__exit__, None, None)
    s = socket.create_connection((HOST, server.port))
    self.addCleanup(s.close)
    s = test_wrap_socket(s, suppress_ragged_eofs=False)
    self.addCleanup(s.close)
    s.send(b'data')
    self.assertEqual(s.recv(0), b'')
    self.assertEqual(s.read(0), b'')
    self.assertEqual(s.read(), b'data')
    s.setblocking(False)
    self.assertEqual(s.recv(0), b'')
    self.assertEqual(s.recv_into(bytearray()), 0)
