# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_is_socket_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE, 'mysock')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    self.addCleanup(sock.close)
    try:
        sock.bind(str(P))
    except OSError as e:
        if isinstance(e, PermissionError) or 'AF_UNIX path too long' in str(e):
            self.skipTest('cannot bind Unix socket: ' + str(e))
    self.assertTrue(P.is_socket())
    self.assertFalse(P.is_fifo())
    self.assertFalse(P.is_file())
    self.assertIs(self.cls(BASE, 'mysock\udfff').is_socket(), False)
    self.assertIs(self.cls(BASE, 'mysock\x00').is_socket(), False)
