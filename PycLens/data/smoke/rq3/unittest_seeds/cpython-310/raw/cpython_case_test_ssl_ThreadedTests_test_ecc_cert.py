# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_ecc_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.load_verify_locations(SIGNING_CA)
    client_context.set_ciphers('ECDHE:ECDSA:!NULL:!aRSA')
    hostname = SIGNED_CERTFILE_ECC_HOSTNAME
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.load_cert_chain(SIGNED_CERTFILE_ECC)
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            cert = s.getpeercert()
            self.assertTrue(cert, "Can't get peer certificate.")
            cipher = s.cipher()[0].split('-')
            self.assertTrue(cipher[:2], ('ECDHE', 'ECDSA'))
