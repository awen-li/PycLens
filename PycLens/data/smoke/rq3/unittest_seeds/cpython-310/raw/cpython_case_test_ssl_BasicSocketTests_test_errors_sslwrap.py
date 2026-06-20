# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_errors_sslwrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    self.assertRaisesRegex(ValueError, 'certfile must be specified', ssl.wrap_socket, sock, keyfile=CERTFILE)
    self.assertRaisesRegex(ValueError, 'certfile must be specified for server-side operations', ssl.wrap_socket, sock, server_side=True)
    self.assertRaisesRegex(ValueError, 'certfile must be specified for server-side operations', ssl.wrap_socket, sock, server_side=True, certfile='')
    with ssl.wrap_socket(sock, server_side=True, certfile=CERTFILE) as s:
        self.assertRaisesRegex(ValueError, "can't connect in server-side mode", s.connect, (HOST, 8080))
    with self.assertRaises(OSError) as cm:
        with socket.socket() as sock:
            ssl.wrap_socket(sock, certfile=NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    with self.assertRaises(OSError) as cm:
        with socket.socket() as sock:
            ssl.wrap_socket(sock, certfile=CERTFILE, keyfile=NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    with self.assertRaises(OSError) as cm:
        with socket.socket() as sock:
            ssl.wrap_socket(sock, certfile=NONEXISTINGCERT, keyfile=NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
