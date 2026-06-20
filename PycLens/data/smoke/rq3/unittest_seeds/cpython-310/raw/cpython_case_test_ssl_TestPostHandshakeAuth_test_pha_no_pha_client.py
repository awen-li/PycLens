# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_pha_no_pha_client

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context.post_handshake_auth = True
    server_context.verify_mode = ssl.CERT_REQUIRED
    client_context.load_cert_chain(SIGNED_CERTFILE)
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            with self.assertRaisesRegex(ssl.SSLError, 'not server'):
                s.verify_client_post_handshake()
            s.write(b'PHA')
            self.assertIn(b'extension not received', s.recv(1024))
