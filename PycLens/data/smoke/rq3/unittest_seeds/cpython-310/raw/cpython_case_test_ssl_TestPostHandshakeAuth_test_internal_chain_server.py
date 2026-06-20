# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestPostHandshakeAuth_test_internal_chain_server

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.load_cert_chain(SIGNED_CERTFILE)
    server_context.verify_mode = ssl.CERT_REQUIRED
    server_context.maximum_version = ssl.TLSVersion.TLSv1_2
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            s.write(b'VERIFIEDCHAIN\n')
            res = s.recv(1024)
            self.assertEqual(res, b'\x02\n')
            s.write(b'UNVERIFIEDCHAIN\n')
            res = s.recv(1024)
            self.assertEqual(res, b'\x02\n')
