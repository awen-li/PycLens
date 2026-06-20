# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_msg_callback_tls12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    msg = []

    def msg_cb(conn, direction, version, content_type, msg_type, data):
        self.assertIsInstance(conn, ssl.SSLSocket)
        self.assertIsInstance(data, bytes)
        self.assertIn(direction, {'read', 'write'})
        msg.append((direction, version, content_type, msg_type))
    client_context._msg_callback = msg_cb
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
    self.assertIn(('read', TLSVersion.TLSv1_2, _TLSContentType.HANDSHAKE, _TLSMessageType.SERVER_KEY_EXCHANGE), msg)
    self.assertIn(('write', TLSVersion.TLSv1_2, _TLSContentType.CHANGE_CIPHER_SPEC, _TLSMessageType.CHANGE_CIPHER_SPEC), msg)
