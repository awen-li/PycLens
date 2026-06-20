# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_version_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with ThreadedEchoServer(CERTFILE, ssl_version=ssl.PROTOCOL_TLS_SERVER, chatty=False) as server:
        with context.wrap_socket(socket.socket()) as s:
            self.assertIs(s.version(), None)
            self.assertIs(s._sslobj, None)
            s.connect((HOST, server.port))
            self.assertEqual(s.version(), 'TLSv1.3')
        self.assertIs(s._sslobj, None)
        self.assertIs(s.version(), None)
