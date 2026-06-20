# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTestsSSL_test_ssl_verified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(CAFILE)
    with self.assertRaisesRegex(ssl.CertificateError, "IP address mismatch, certificate is not valid for '127.0.0.1'"):
        with self.reaped_server(SimpleIMAPHandler) as server:
            client = self.imap_class(*server.server_address, ssl_context=ssl_context)
            client.shutdown()
    with self.reaped_server(SimpleIMAPHandler) as server:
        client = self.imap_class('localhost', server.server_address[1], ssl_context=ssl_context)
        client.shutdown()
