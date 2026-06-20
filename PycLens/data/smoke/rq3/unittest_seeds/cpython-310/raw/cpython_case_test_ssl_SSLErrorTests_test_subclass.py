# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SSLErrorTests_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with socket.create_server(('127.0.0.1', 0)) as s:
        c = socket.create_connection(s.getsockname())
        c.setblocking(False)
        with ctx.wrap_socket(c, False, do_handshake_on_connect=False) as c:
            with self.assertRaises(ssl.SSLWantReadError) as cm:
                c.do_handshake()
            s = str(cm.exception)
            self.assertTrue(s.startswith('The operation did not complete (read)'), s)
            self.assertEqual(cm.exception.errno, ssl.SSL_ERROR_WANT_READ)
