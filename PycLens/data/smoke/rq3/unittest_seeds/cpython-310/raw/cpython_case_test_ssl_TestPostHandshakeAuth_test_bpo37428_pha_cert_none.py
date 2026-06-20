# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_bpo37428_pha_cert_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hostname = SIGNED_CERTFILE_HOSTNAME
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.post_handshake_auth = True
    client_context.load_cert_chain(SIGNED_CERTFILE)
    client_context.check_hostname = False
    client_context.verify_mode = ssl.CERT_NONE
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.load_cert_chain(SIGNED_CERTFILE)
    server_context.load_verify_locations(SIGNING_CA)
    server_context.post_handshake_auth = True
    server_context.verify_mode = ssl.CERT_REQUIRED
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            s.write(b'HASCERT')
            self.assertEqual(s.recv(1024), b'FALSE\n')
            s.write(b'PHA')
            self.assertEqual(s.recv(1024), b'OK\n')
            s.write(b'HASCERT')
            self.assertEqual(s.recv(1024), b'TRUE\n')
            self.assertEqual(s.getpeercert(), {})
