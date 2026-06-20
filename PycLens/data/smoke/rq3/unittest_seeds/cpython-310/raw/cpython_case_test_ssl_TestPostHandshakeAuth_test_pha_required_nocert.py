# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_pha_required_nocert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context.post_handshake_auth = True
    server_context.verify_mode = ssl.CERT_REQUIRED
    client_context.post_handshake_auth = True

    def msg_cb(conn, direction, version, content_type, msg_type, data):
        if support.verbose and content_type == _TLSContentType.ALERT:
            info = (conn, direction, version, content_type, msg_type, data)
            sys.stdout.write(f'TLS: {info!r}\n')
    server_context._msg_callback = msg_cb
    client_context._msg_callback = msg_cb
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname, suppress_ragged_eofs=False) as s:
            s.connect((HOST, server.port))
            s.write(b'PHA')
            with self.assertRaisesRegex(ssl.SSLError, '(certificate required|EOF occurred)'):
                data = s.recv(1024)
                self.assertEqual(data, b'OK\n')
                s.write(b'HASCERT')
                s.recv(1024)
